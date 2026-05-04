PATTERNS = [
    # ========================
    # ERROR
    # ========================
    {
        "name": "AWS Access Key ID",
        "pattern": r"\bAKIA[0-9A-Z]{16}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Stripe Secret Key",
        "pattern": r"\bsk_live_[A-Za-z0-9]{24}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Stripe Publishable Key",
        "pattern": r"\bpk_live_[A-Za-z0-9]{24}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Stripe Restricted Key",
        "pattern": r"\brk_live_[A-Za-z0-9]{24}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Stripe Client Secret",
        "pattern": r"\bcs_live_[A-Za-z0-9]{32}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "GitHub Personal Access Token",
        "pattern": r"\bghp_[A-Za-z0-9_]{36}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "GitHub OAuth Token",
        "pattern": r"\bgho_[A-Za-z0-9_]{36}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "GitHub App Token",
        "pattern": r"\bghu_[A-Za-z0-9_]{36}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "GitHub Installation Token",
        "pattern": r"\bghs_[A-Za-z0-9_]{36}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "GitLab Personal Access Token",
        "pattern": r"\bglpat-[A-Za-z0-9]{20}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Slack Bot Token",
        "pattern": r"\bxoxb-[0-9]{12}-[0-9]{12}-[A-Za-z0-9]{24}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Slack User Token",
        "pattern": r"\bxoxp-[0-9]{12}-[0-9]{12}-[0-9]{12}-[A-Za-z0-9]{24}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "SendGrid API Key",
        "pattern": r"\bSG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Twilio SID",
        "pattern": r"\bAC[0-9a-fA-F]{32}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Twilio API Key SID",
        "pattern": r"\bSK[0-9a-fA-F]{32}\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "PostgreSQL Connection String with Credentials",
        "pattern": r"\bpostgres(?:ql)?://[^:\s]+:[^@\s]+@[^/\s]+(?:/\S*)?\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "MySQL Connection String with Credentials",
        "pattern": r"\bmysql://[^:\s]+:[^@\s]+@[^/\s]+(?:/\S*)?\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "MongoDB Connection String with Credentials",
        "pattern": r"\bmongodb(?:\+srv)?://[^:\s]+:[^@\s]+@[^/\s]+(?:/\S*)?\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Supabase API Key",
        "pattern": r"\beyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\b",
        "severity": "error",
        "confidence": "high",
    },
    {
        "name": "Gmail App Password",
        "pattern": r"\b[a-z]{4}\s[a-z]{4}\s[a-z]{4}\s[a-z]{4}\b",
        "severity": "error",
        "confidence": "high",
    },
    # ========================
    # WARNING
    # ========================
    {
        "name": "AWS Secret Access Key (Generic)",
        "pattern": r"\b[A-Za-z0-9/+=]{40}\b",
        "severity": "warning",
        "confidence": "medium",
    },
    {
        "name": "JWT Token",
        "pattern": r"\b[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\b",
        "severity": "warning",
        "confidence": "medium",
    },
    {
        "name": "Generic API Key (Hex 32)",
        "pattern": r"\b[a-f0-9]{32}\b",
        "severity": "warning",
        "confidence": "medium",
    },
    {
        "name": "Generic DB URL with Credentials",
        "pattern": r"\b[a-zA-Z]+://[^:\s]+:[^@\s]+@[^/\s]+",
        "severity": "warning",
        "confidence": "medium",
    },
    {
        "name": "Generic High-Entropy Base64",
        "pattern": r"\b[A-Za-z0-9+/]{40,}={0,2}\b",
        "severity": "warning",
        "confidence": "medium",
    },
    # ========================
    # CONTEXTUAL
    # ========================
    {
        "name": "Suspicious Variable Name",
        "pattern": r"(?i)(api[_-]?key|secret|token|password)\s*=\s*.+",
        "severity": "info",
        "confidence": "low",
    },
]
