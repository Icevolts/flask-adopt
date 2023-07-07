from flask import Flask,render_template,url_for,redirect
from models import db, connect_db,Pet
from forms import AddPetForm,EditPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'f724'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.debug = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    '''Load hompage of Pets'''
    pets = Pet.query.all()
    return render_template('homepage.html',pets=pets)

@app.route('/add', methods=['GET','POST'])
def new_pet():
    '''Show form for adding new pet'''
    form = AddPetForm()
    if form.validate_on_submit():
        data = {k:v for k,v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    '''Show form to edit pet info'''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        return redirect(url_for('home'))
    
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)