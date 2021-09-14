from reseau import Reseau

res = Reseau()

res.set_erreur(0.5)

res.print_data()
res.set_couche(3)
res.add_all_neurone([4,4,2])
res.creer_reseau()
res.print_all()

res.learn([1,0,1,0],[1,0])


res.print_last_couche()
