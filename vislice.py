import bottle
import model

SKRIVNOST = 'moja skrivnost'


visilice = model.Vislice(model.DATOTEKA_S_STANJEM)


@bottle.get("/")
def index():
    return bottle.template("index.tpl")


@bottle.post("/nova-igra/")
def nova_igra():
    id_igre = visilice.nova_igra()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    trenutna_igra, trenutno_stanje = visilice.igre[id_igre]
    return bottle.template("igra.tpl", igra=trenutna_igra, stanje=trenutno_stanje)

@bottle.post("/igra/")
def ugibaj_na_igri():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    ugibana = bottle.request.forms["crka"]

    visilice.ugibaj(id_igre,ugibana)

    return bottle.redirect("/igra/")

@bottle.get("/img/<file_path:path>")
def img_static(file_path):
    return bottle.static_file(file_path, "img")
#hhh



bottle.run(reloader=True,debug=True)
