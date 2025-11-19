from flask import Flask, render_template
from models import db
import models   # garante que as classes sejam importadas e mapeadas

# ============================================
# CONFIGURAÇÃO DA APLICAÇÃO
# ============================================
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa o banco
db.init_app(app)

# Cria as tabelas automaticamente no início
with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")


# ============================================
# ROTAS PRINCIPAIS DO SITE
# ============================================

@app.route("/")
def home():
    from models import News, Player, Match, Product, Sponsor

    breaking_news = News.query.order_by(News.created_at.desc()).limit(6).all()
    squad = Player.query.all()
    matches = Match.query.order_by(Match.date.asc()).limit(5).all()
    products = Product.query.all()
    sponsors = Sponsor.query.all()

    return render_template(
        "home.html",
        title="Início",
        breaking_news=breaking_news,
        players=squad,
        matches=matches,
        products=products,
        sponsors=sponsors,
        active_page="home"
    )


@app.route("/time")
def time():
    from models import Player
    players = Player.query.all()
    return render_template(
        "time.html", 
        title="Nosso Time", 
        players=players,
        active_page="time"
    )


@app.route("/loja")
def loja():
    from models import Product
    products = Product.query.all()
    return render_template(
        "loja.html", 
        title="Loja Oficial", 
        products=products,
        active_page="loja"
    )


@app.route("/parceiros")
def parceiros():
    from models import Sponsor
    sponsors = Sponsor.query.all()
    return render_template(
        "parceiros.html", 
        title="Parceiros", 
        sponsors=sponsors,
        active_page="parceiros"
    )


@app.route("/noticias")
def noticias():
    from models import News
    all_news = News.query.order_by(News.created_at.desc()).all()
    return render_template(
        "noticias.html", 
        title="Notícias", 
        noticias=all_news,
        active_page="noticias"
    )


@app.route("/agenda")
def agenda():
    from models import Match
    matches = Match.query.order_by(Match.date.asc()).all()
    return render_template(
        "agenda.html", 
        title="Agenda de Jogos", 
        matches=matches,
        active_page="agenda"
    )


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html", title="Cadastro", active_page="cadastro")


@app.route("/login")
def login():
    return render_template("login.html", title="Login", active_page="login")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    app.run(debug=True)
