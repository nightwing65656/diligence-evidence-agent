import pytest

from diligence_agent.evidence import Claim, EvidenceSpan, unsupported_claim_rate


def make_span(text: str = "Revenue was $100 million.") -> EvidenceSpan:
    return EvidenceSpan.create("doc1", "https://www.sec.gov/example", 12, text)


def test_untampered_evidence_verifies() -> None:
    assert make_span().verify()


def test_tampered_evidence_is_detected() -> None:
    tampered = make_span().model_copy(update={"text": "Revenue was $900 million."})
    assert not tampered.verify()


def test_claim_without_evidence_is_unsupported() -> None:
    assert not Claim(claim_id="c1", statement="Margins expanded.").is_supported


def test_unsupported_rate() -> None:
    good = Claim(claim_id="c1", statement="Revenue was $100M.", evidence=(make_span(),))
    bad = Claim(claim_id="c2", statement="Margins expanded.")
    assert unsupported_claim_rate([good, bad]) == pytest.approx(0.5)