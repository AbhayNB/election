from models import VidhanSabha, Booth, BoothData
from config import app, render_template, request, redirect, url_for,flash,jsonify,db

#======= Routs ====
@app.route('/view_booth', methods=['POST'])
def view_booth():
    action="Update"
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
            if booth_data:
                return render_template('view_booth.html', booth=booth,booth_data=booth_data,action=action)
            flash('Booth data does not exist you please create one', 'info')  # Flash success message
            return redirect('/')
        return render_template('wrongboothno.html')
@app.route('/base')
def base():
    # Passing data to the template
    return render_template('base.html')
@app.route('/demo')
def demo():
    # Passing data to the template
    return render_template('demo.html')
@app.route('/')
def index():
    # Fetching data from the database
    vidhan_sabhas = VidhanSabha.query.all()
    
    # Passing data to the template
    return render_template('index.html', vidhan_sabhas=vidhan_sabhas)
@app.route('/update')
def update():
    # Fetching data from the database
    vidhan_sabhas = VidhanSabha.query.all()
    
    # Passing data to the template
    return render_template('update.html', vidhan_sabhas=vidhan_sabhas)
@app.route('/view')
def view():
    # Fetching data from the database
    vidhan_sabhas = VidhanSabha.query.all()
    
    # Passing data to the template
    return render_template('view.html', vidhan_sabhas=vidhan_sabhas)
@app.route('/booth_details', methods=['POST'])
def booth_details():
    action="Create"
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
            if booth_data:
                flash('Booth data already exist you may want to update it', 'danger')  # Flash success message
                return redirect('/update')
            return render_template('booth_details.html', booth=booth,booth_data=booth_data,action=action)
        return render_template('wrongboothno.html')
@app.route('/booth_details_update', methods=['POST'])
def booth_details_update():
    action="Update"
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
            if booth_data:
                return render_template('booth_details.html', booth=booth,booth_data=booth_data,action=action)
            flash('Booth data does not exist you please create one', 'info')  # Flash success message
            return redirect('/')
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
    vidhan_sabha = VidhanSabha.query.filter_by(id=vidhan_sabha_id).first()
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
    df = df.drop(columns=['id','booth_id'])
    # Export the DataFrame to an Excel file
    cols = list(df.columns)
    cols.insert(0, cols.pop(cols.index('booth_number')))
    df = df[cols]
    excel_file = f'vidhan_sabha_{vidhan_sabha_id}_data.xlsx'
    df.to_excel(excel_file, index=False)

    # Send the Excel file as a response
    #return render_template('allbooths_v.html', tables=[df.to_html(classes='data')], titles=df.columns.values,vidhan_sabha=vidhan_sabha)
    return send_file(excel_file, as_attachment=True)
@app.route('/add_booth', methods=['GET', 'POST'])
def add_booth():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)
            with db.session.no_autoflush:
                for index, row in df.iterrows():
                    booth = Booth.query.filter_by(booth_number=row['booth_number'],vidhan_sabha_id=row["vidhan_sabha_id"]).first()
                    if booth:
                        booth.name = row['name']
                        booth.total_voters = row['total_voters']
                        booth.male_voters = row['male_voters']
                        booth.female_voters = row['female_voters']
                        booth.other_voters = row['other_voters']
                    else:
                        new_booth = Booth(
                            name=row['name'],
                            booth_number=row['booth_number'],
                            total_voters=row['total_voters'],
                            male_voters=row['male_voters'],
                            female_voters=row['female_voters'],
                            other_voters=row['other_voters'],
                            vidhan_sabha_id=row['vidhan_sabha_id']
                        )
                        db.session.add(new_booth)
            db.session.commit()
            return 'Booth data updated successfully.'
        else:
            return 'Invalid file format. Please upload an Excel file.'
    return render_template('update_booth.html')

@app.route('/generate_report/<int:vidhan_sabha_id>', methods=['GET','POST'])
def generate_report(vidhan_sabha_id):
    vidhan_sabha = VidhanSabha.query.filter_by(id=vidhan_sabha_id).first()
    sort_column=None
    filter_column=None
    filter_value=None
    if request.method == 'POST':
        sort_column = request.form['sort_column'] if request.form['sort_column'] else None
        sort_order = request.form['sort_order'] if request.form['sort_order'] else None
        filter_column = request.form['filter_column'] if request.form['filter_column'] else None
        filter_value = request.form['filter_value'] if request.form['filter_value'] else None
    # Query parameters for filtering and sorting
    # filter_column = request.args.get('filter_column')
    # filter_value = request.args.get('filter_value')
    # sort_column = request.args.get('sort_column')
    # sort_order = request.args.get('sort_order')

    # Base query to retrieve booth data
    base_query = db.session.query(Booth, BoothData).\
        join(BoothData, Booth.id == BoothData.booth_id).\
        filter(Booth.vidhan_sabha_id == vidhan_sabha_id)
    
    # Apply filtering if filter parameters are provided
    if filter_column and filter_value:
        base_query = base_query.filter(getattr(Booth, filter_column) == filter_value)

    # Apply sorting if sort parameters are provided
    if sort_column:
        if sort_order == 'asc':
            base_query = base_query.order_by(getattr(BoothData, sort_column).asc())
        elif sort_order == 'desc':
            base_query = base_query.order_by(getattr(BoothData, sort_column).desc())

    # Execute the query
    booth_data = base_query.all()

    # Create DataFrame
    data = []
    columns = [column.key for column in Booth.__table__.columns] + [column.key for column in BoothData.__table__.columns]
    
    for booth, booth_data in booth_data:
        data.append([getattr(booth, col) for col in columns[:len(Booth.__table__.columns)]] + 
                    [getattr(booth_data, col) for col in columns[len(Booth.__table__.columns):]])
    
    df = pd.DataFrame(data, columns=columns)
    df = df.drop(columns=['id', 'booth_id'])
    df = df.rename(columns={'booth_number': 'Booth Number'})  # Rename 'booth_number' to match the HTML template

    # Export the DataFrame to an Excel file
    excel_file = f'vidhan_sabha_{vidhan_sabha_id}_data.xlsx'

    # Render the template with DataFrame HTML representation and parameters
    return render_template('allbooths_v.html', tables=[df.to_html(classes='data')], titles=df.columns.values, vidhan_sabha=vidhan_sabha)
