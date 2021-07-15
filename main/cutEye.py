#método que corta a sobrancelha da img 
def cut_eyebrows(img): 
	altura, largura = img.shape[:2] 
	sobrancelha_h = int(altura / 4)
	pontas = int(largura/5)
	img = img[sobrancelha_h:altura, pontas:largura-pontas]
	return img