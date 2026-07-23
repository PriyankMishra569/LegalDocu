from pydantic import BaseModel, Field
from typing import List, Optional


class Clause(BaseModel):
    title: str
    description: str
    importance: str  # High, Medium, Low


class Obligation(BaseModel):
    party: str
    obligation: str
    deadline: Optional[str] = None


class Deadline(BaseModel):
    event: str
    date: str


class Risk(BaseModel):
    title: str
    severity: str      # Low / Medium / High
    explanation: str


class LegalDocument(BaseModel):

    # Basic Information
    is_legal: bool
    document_type: str
    title: str = ""
    summary: str

    # Parties
    parties: List[str] = Field(default_factory=list)

    # Purpose
    purpose: str = ""

    # Clauses
    important_clauses: List[Clause] = Field(default_factory=list)

    # Obligations
    obligations: List[Obligation] = Field(default_factory=list)

    # Deadlines
    deadlines: List[Deadline] = Field(default_factory=list)

    # Risks
    risks: List[Risk] = Field(default_factory=list)

    # Overall Risk Analysis
    risk_score: int = 0
    risk_level: str = "Low"

    # Recommendations
    recommendations: List[str] = Field(default_factory=list)

    # Missing Clauses
    missing_clauses: List[str] = Field(default_factory=list)

    # Governing Law
    governing_law: str = ""

    # Jurisdiction
    jurisdiction: str = ""

    # Duration
    effective_date: str = ""
    expiration_date: str = ""

    # Financial Terms
    payment_terms: str = ""
    penalty_clause: str = ""

    # Termination
    termination_clause: str = ""

    # Confidentiality
    confidentiality_clause: bool = False

    # Arbitration
    arbitration_clause: bool = False

    # Force Majeure
    force_majeure: bool = False

    # Overall AI Opinion
    overall_assessment: str = ""

    # If not legal
    reason: str = ""