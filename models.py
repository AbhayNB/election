from config import db

class VidhanSabha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    booths = db.relationship("Booth", backref="vidhan_sabha", lazy=True)

    def __repr__(self):
        return f"{self.id} - {self.name}"

class Booth(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    booth_number = db.Column(db.Integer, nullable=False)
    total_voters = db.Column(db.Integer, nullable=False)
    male_voters = db.Column(db.Integer, nullable=False)
    female_voters = db.Column(db.Integer, nullable=False)
    other_voters = db.Column(db.Integer, nullable=False)
    vidhan_sabha_id = db.Column(db.Integer, db.ForeignKey("vidhan_sabha.id"), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.name}"

class BoothData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booth_id = db.Column(db.Integer, db.ForeignKey("booth.id"), nullable=False)
    male_voted = db.Column(db.Integer, nullable=True)  # Nullable field
    female_voted = db.Column(db.Integer, nullable=True)  # Nullable field
    other_voted = db.Column(db.Integer, nullable=True)  # Nullable field
    total_voted = db.Column(db.Integer, nullable=True)  # Nullable field
    vote_percentage = db.Column(db.Float, nullable=True)  # Nullable field
    tender_votes = db.Column(db.Integer, nullable=True)  # Nullable field
    challenge_votes = db.Column(db.Integer, nullable=True)  # Nullable field
    proxy_votes = db.Column(db.Integer, nullable=True)  # Nullable field
    voters_with_assistance_count = db.Column(db.Integer, nullable=True)  # Nullable field
    voters_with_EPIC_count = db.Column(db.Integer, nullable=True)  # Nullable field
    voters_with_alternative_documents_count = db.Column(db.Integer, nullable=True)  # Nullable field
    rule49_voters = db.Column(db.Integer, nullable=True)  # Nullable field
    mock_polling_voters_count = db.Column(db.Integer, nullable=True)  # Nullable field
    agent_present = db.Column(db.Integer, nullable=True)  # Nullable field
    migrant_voters = db.Column(db.Integer, nullable=True)  # Nullable field
    bu_used = db.Column(db.Integer, nullable=True)  # Nullable field
    cu_used = db.Column(db.Integer, nullable=True)  # Nullable field
    vvpat_used = db.Column(db.Integer, nullable=True)  # Nullable field
    bu_cu_vvpat_changed = db.Column(db.String(3), nullable=True)  # Nullable field
    bu_cu_vvpat_change_time = db.Column(db.String(100), nullable=True)  # Nullable field
    eds_voters_voted = db.Column(db.Integer, nullable=True)  # Nullable field
    asd_total_voters = db.Column(db.Integer, nullable=True)  # Nullable field
    asd_voters_voted = db.Column(db.Integer, nullable=True)  # Nullable field
    ballots_distributed_at_6PM = db.Column(db.Integer, nullable=True)  # Nullable field
    incidents_reported = db.Column(db.Text, nullable=True)  # Nullable field
    complaints_reported = db.Column(db.Text, nullable=True)  # Nullable field


    booth = db.relationship("Booth", backref="update_info", lazy=True)

    def __repr__(self):
        return f"Booth Update ID: {self.id}, Booth ID: {self.booth_id}"
