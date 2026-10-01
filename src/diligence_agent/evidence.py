from __future__ import annotations

import hashlib

from pydantic import BaseModel, ConfigDict


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class EvidenceSpan(BaseModel):
    model_config = ConfigDict(frozen=True)
    document_id: str
    source_url: str
    page: int
    text: str
    text_sha256: str

    @classmethod
    def create(cls, document_id: str, source_url: str, page: int, text: str) -> EvidenceSpan:
        return cls(
            document_id=document_id,
            source_url=source_url,
            page=page,
            text=text,
            text_sha256=sha256_text(text),
        )

    def verify(self) -> bool:
        return sha256_text(self.text) == self.text_sha256


class Claim(BaseModel):
    model_config = ConfigDict(frozen=True)
    claim_id: str
    statement: str
    evidence: tuple[EvidenceSpan, ...] = ()

    @property
    def is_supported(self) -> bool:
        return bool(self.evidence) and all(e.verify() for e in self.evidence)


def unsupported_claim_rate(claims: list[Claim]) -> float:
    if not claims:
        return 0.0
    return sum(not c.is_supported for c in claims) / len(claims)
