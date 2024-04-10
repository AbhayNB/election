from flask import Flask, render_template, request, redirect, url_for,flash,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Real list of Vidhan Sabha constituencies in Hindi
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///election2.db'
db = SQLAlchemy(app)
app.secret_key = 'jbp_election'
class VidhanSabha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    booths = db.relationship("Booth", backref="vidhan_sabha", lazy=True)

    def __repr__(self):
        return f"{self.id} - {self.name}"

class Booth(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    booth_building_name= db.Column(db.String(200), nullable=False)
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

#======= Routs ====

@app.route('/')
def index():
    # Fetching data from the database
    vidhan_sabhas = VidhanSabha.query.all()
    
    # Passing data to the template
    return render_template('index.html', vidhan_sabhas=vidhan_sabhas)

@app.route('/booth_details', methods=['POST'])
def booth_details():
    if request.method == 'POST':
        # Extract data from the form
        try:
            vidhan_sabha_id = request.form['vidhan_sabha']
            booth_number = request.form['boothNumber']
        except:
            return render_template('wrongboothno.html',msg="Select AC to move ahed")
        # Query the database to get details of the selected booth
        booth = Booth.query.filter_by(vidhan_sabha_id=vidhan_sabha_id, booth_number=booth_number).first()
        # Render a template with the details of the selected booth
        if booth:
            booth_data = BoothData.query.filter_by(booth_id=booth.id).first()
            return render_template('booth_details.html', booth=booth,booth_data=booth_data)
        return render_template('wrongboothno.html')
@app.route('/update_booth_data', methods=['POST'])
def update_booth_data():
    if request.method == 'POST':
        booth_id = request.form['booth_id'] 
        male_voted = request.form['male_voted'] if request.form['male_voted'] else None
        female_voted = request.form['female_voted'] if request.form['female_voted'] else None
        other_voted = request.form['other_voted'] if request.form['other_voted'] else None
        total_voted = request.form['total_voted'] if request.form['total_voted'] else None
        vote_percentage = request.form['vote_percentage'] if request.form['vote_percentage'] else None
        tender_votes = request.form['tender_votes'] if request.form['tender_votes'] else None
        challenge_votes = request.form['challenge_votes'] if request.form['challenge_votes'] else None
        proxy_votes = request.form['proxy_votes'] if request.form['proxy_votes'] else None
        voters_with_assistance_count = request.form['voters_with_assistance_count'] if request.form['voters_with_assistance_count'] else None
        voters_with_EPIC_count = request.form['voters_with_EPIC_count'] if request.form['voters_with_EPIC_count'] else None
        voters_with_alternative_documents_count = request.form['voters_with_alternative_documents_count'] if request.form['voters_with_alternative_documents_count'] else None
        rule49_voters = request.form['rule49_voters'] if request.form['rule49_voters'] else None
        mock_polling_voters_count = request.form['mock_polling_voters_count'] if request.form['mock_polling_voters_count'] else None
        agent_present = request.form['agent_present'] if request.form['agent_present'] else None
        migrant_voters = request.form['migrant_voters'] if request.form['migrant_voters'] else None
        bu_used = request.form['bu_used'] if request.form['bu_used'] else None
        cu_used = request.form['cu_used'] if request.form['cu_used'] else None
        vvpat_used = request.form['vvpat_used'] if request.form['vvpat_used'] else None
        bu_cu_vvpat_changed = request.form['bu_cu_vvpat_changed'] if request.form['bu_cu_vvpat_changed'] else None
        bu_cu_vvpat_change_time = request.form['bu_cu_vvpat_change_time'] if request.form['bu_cu_vvpat_change_time'] else None
        eds_voters_voted = request.form['eds_voters_voted'] if request.form['eds_voters_voted'] else None
        asd_total_voters = request.form['asd_total_voters'] if request.form['asd_total_voters'] else None
        asd_voters_voted = request.form['asd_voters_voted'] if request.form['asd_voters_voted'] else None
        ballots_distributed_at_6PM = request.form['ballots_distributed_at_6PM'] if request.form['ballots_distributed_at_6PM'] else None
        incidents_reported = request.form['incidents_reported'] if request.form['incidents_reported'] else None
        complaints_reported = request.form['complaints_reported'] if request.form['complaints_reported'] else None

        booth_data = BoothData.query.filter_by(booth_id=booth_id).first()

        if booth_data is None:
            # Create a new BoothData entry
            booth_data = BoothData(
                booth_id=booth_id,
                male_voted=male_voted,
                female_voted=female_voted,
                other_voted=other_voted,
                total_voted=total_voted,
                vote_percentage=vote_percentage,
                tender_votes=tender_votes,
                challenge_votes=challenge_votes,
                proxy_votes=proxy_votes,
                voters_with_assistance_count=voters_with_assistance_count,
                voters_with_EPIC_count=voters_with_EPIC_count,
                voters_with_alternative_documents_count=voters_with_alternative_documents_count,
                rule49_voters=rule49_voters,
                mock_polling_voters_count=mock_polling_voters_count,
                agent_present=agent_present,
                migrant_voters=migrant_voters,
                bu_used=bu_used,
                cu_used=cu_used,
                vvpat_used=vvpat_used,
                bu_cu_vvpat_changed=bu_cu_vvpat_changed,
                bu_cu_vvpat_change_time=bu_cu_vvpat_change_time,
                eds_voters_voted=eds_voters_voted,
                asd_total_voters=asd_total_voters,
                asd_voters_voted=asd_voters_voted,
                ballots_distributed_at_6PM=ballots_distributed_at_6PM,
                incidents_reported=incidents_reported,
                complaints_reported=complaints_reported
            )
            db.session.add(booth_data)
        else:
            # Update existing BoothData entry
            booth_data.male_voted = male_voted
            booth_data.female_voted = female_voted
            booth_data.other_voted = other_voted
            booth_data.total_voted = total_voted
            booth_data.vote_percentage = vote_percentage
            booth_data.tender_votes = tender_votes
            booth_data.challenge_votes = challenge_votes
            booth_data.proxy_votes = proxy_votes
            booth_data.voters_with_assistance_count = voters_with_assistance_count
            booth_data.voters_with_EPIC_count = voters_with_EPIC_count
            booth_data.voters_with_alternative_documents_count = voters_with_alternative_documents_count
            booth_data.rule49_voters = rule49_voters
            booth_data.mock_polling_voters_count = mock_polling_voters_count
            booth_data.agent_present = agent_present
            booth_data.migrant_voters = migrant_voters
            booth_data.bu_used = bu_used
            booth_data.cu_used = cu_used
            booth_data.vvpat_used = vvpat_used
            booth_data.bu_cu_vvpat_changed = bu_cu_vvpat_changed
            booth_data.bu_cu_vvpat_change_time = bu_cu_vvpat_change_time
            booth_data.eds_voters_voted = eds_voters_voted
            booth_data.asd_total_voters = asd_total_voters
            booth_data.asd_voters_voted = asd_voters_voted
            booth_data.ballots_distributed_at_6PM = ballots_distributed_at_6PM
            booth_data.incidents_reported = incidents_reported
            booth_data.complaints_reported = complaints_reported

        try:
            # Commit the changes to the database
            db.session.commit()
            flash('Booth data updated successfully', 'success')  # Flash success message
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while updating booth data', 'error')  # Flash error message
            return redirect('/')
    else:
        return jsonify({'error': 'Method Not Allowed'}), 405


from flask import send_file
import pandas as pd
@app.route('/generate_excel')
def generate_excel_page():
    vidhan_sabhas = VidhanSabha.query.all()
    return render_template('getexel.html',vidhan_sabhas=vidhan_sabhas)
@app.route('/generate_excel/<int:vidhan_sabha_id>')
def generate_excel(vidhan_sabha_id):
    # Query the database to get the booths and their data for the given Vidhan Sabha ID
    booth_data = db.session.query(Booth, BoothData).\
        join(BoothData, Booth.id == BoothData.booth_id).\
        filter(Booth.vidhan_sabha_id == vidhan_sabha_id).\
        all()

    # Create a DataFrame to hold the combined data
    data = []
    columns = [column.key for column in Booth.__table__.columns] + [column.key for column in BoothData.__table__.columns]
    
    for booth, booth_data in booth_data:
        data.append([getattr(booth, col) for col in columns[:len(Booth.__table__.columns)]] + 
                    [getattr(booth_data, col) for col in columns[len(Booth.__table__.columns):]])
    
    df = pd.DataFrame(data, columns=columns)

    # Export the DataFrame to an Excel file
    excel_file = f'vidhan_sabha_{vidhan_sabha_id}_data.xlsx'
    df.to_excel(excel_file, index=False)

    # Send the Excel file as a response
    return send_file(excel_file, as_attachment=True)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)