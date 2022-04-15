class Matrice: #klase su skupovi funkcija koje cemo koristiti za manipuliranje objekta tj. matrica
    
    def __init__(self, velicina):  #funkcija za unos veličine matrice 'self'. init je konstruktor nekog određenog objekta gdje ćemo upisivati veličinu naših matrica
        self.red, self.kolona = velicina.split() 
        
    def novamat(self):
        self.matrica = [[int(y) for y in input().split()] for x in range(int(self.red))]     ##funkcija za stvaranje matrice
        
    def zbrajanje(self, mat):
        if self.red == mat.red and self.kolona == mat.kolona:
            rezultat = [[self.matrica[x][y] + mat.matrica[x][y] for y in range(len(self.matrica))] for x in
                      range(len(self.matrica))]
            for red in rezultat:
                for broj in red:
                    print(broj , end=" ")
                print()
        else:
            print("Operacija nije moguća, dimenzije se ne usklađuju!")
    
    def oduzimanje(self, mat):
        if self.red == mat.red and self.kolona == mat.kolona:
            rezultat = [[self.matrica[x][y] - mat.matrica[x][y] for y in range(len(self.matrica))] for x in
                      range(len(self.matrica))]
            for red in rezultat:
                for broj in red:
                    print(broj , end=" ")
                print()
        else:
            print("Operacija nije moguća, dimenzije se ne usklađuju!")
            
    def skalar(self, skalar):
        rezultat = [[self.matrica[x][y] * skalar for y in range(len(self.matrica))] for x in range(len(self.matrica[0]))]
        for red in rezultat:
            for broj in red:
                print(broj , end=" ")
            print()
    
    def mnozenje(self, mat):
        if self.kolona != mat.red:
            print("Operacija nije moguća, dimenzije se ne usklađuju!")
        else: # popravljeno, problem je bio u iteriranju kroz drugu matricu što je zahtjevalo trasponiranje druge matrice. ovo je brža i jednostavnija opcija sa zip() funkcijom. objašnjenje: https://www.programiz.com/python-programming/methods/built-in/zip
            rezultat = [[sum(x*y for x,y in zip(self.matrica_red, mat.matrica_kolona)) for mat.matrica_kolona in zip(*mat.matrica)] for self.matrica_red in (self.matrica)]
            for red in rezultat:
                for broj in red:
                    print(broj, end=" ")
                print()
    
    def transponiranje(self):
        rezultat = [[self.matrica[x][y] for x in range(len(self.matrica))] for y in range(len(self.matrica))]
        for red in rezultat:
            for broj in red:
                print(broj , end=" ")
            print()
    
    @staticmethod
    def determinanta(mat):
        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) == 2:
            determinanta = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
            return determinanta
        else: #koristimo laplace expansion ili cofactor expansion vise na : https://www.statlect.com/matrix-algebra/Laplace-expansion-minors-cofactors-adjoints
            rekdet = 0
            for x, y in enumerate(mat):
                rekrez = mat[0][x] * Matrice.determinanta([[element for indeks, element in enumerate(rekmat) if indeks != x] for rekmat in mat[1:]])
                if x % 2 == 0:
                    rekdet = rekdet + rekrez
                else:
                    rekdet = rekdet - rekrez
            return rekdet

    @staticmethod
    def minor(matx, x, y):
        return [red[:y] + red[y+1:] for red in (matx[:x]+matx[x+1:])]
    
    
    @staticmethod
    def traninv(spon):
        return map(list,zip(*spon))


    def inverz(self):
        if Matrice.determinanta(self) == 0:
            print("Naša matrica nema inverz, determinanta je 0")
        else:
            if len(self) == 2:
                det2x2 = Matrice.determinanta(self)
                inverz2x2 = []
                inverz2x2 = ([[round(float(self[1][1]/det2x2),2), round(float((-1*self[0][1])/det2x2),2)],[round(float((-1*self[1][0])/det2x2),2), round(float(self[0][0]/det2x2),2)]])
                for red in inverz2x2:
                    for broj in red:
                        print(broj , end=" ")
                    print()
            else:
                inverz = []
                for x in range(len(self)):
                    kofaktor = []
                    for y in range(len(self)):
                        minormat = Matrice.minor(self, x, y)
                        kofaktor.append((((-1) ** (x+y))) * Matrice.determinanta(minormat))
                        
                    inverz.append(kofaktor)
                inverz = list(Matrice.traninv(inverz))
                for x in range(len(inverz)):
                    for y in range(len(inverz)):
                        inverz[x][y] = inverz[x][y]/Matrice.determinanta(self)   
                for x in inverz:
                    for y in x:
                        print(round(y,2) , end=" ")
                    print()



class Hill:
    
    @staticmethod
    def novikljuc(kljucic):
        kljucic = [[int(x) for x in input().split()] for x in range(3)]
        return kljucic
    
    @staticmethod
    def provchar(slovo):
        symbols = [' ', '!', '#', '$', '%', '&', '"', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '', '`', '{', '|', '}', '~',"'"]
        for char in slovo:
            if char in symbols:
                return True
            return False
    
    @staticmethod
    def rastav(recenica):
        pomrec = []
        for x in recenica:
            if Hill.provchar(x):
                continue
            else:
                pomrec.append(ord(x.upper())%65)
        return pomrec
    
    @staticmethod
    def kriptiranje(kljucfin, fraza):
        pomocni = []
        privremeni = 0
        sifrat = ''
        
        while len(fraza) >= 0:
            if len(fraza) == 0:
                break
            if len(fraza) == 2:
                fraza.append(0)
            elif len(fraza) == 1:
                fraza.append(0)
                fraza.append(0)
            for x in range(3):
                privremeni = 0
                for y in range(3):
                    privremeni += kljucfin[x][y]*fraza[y]
                pomocni.append(privremeni%26) 
            fraza.reverse()
            fraza.pop()
            fraza.pop()
            fraza.pop()
            fraza.reverse()
        
        sifrat = ''.join(chr(slovo+65) for slovo in pomocni)
        print(sifrat)

    @staticmethod
    def multiverz(determ):
        multinv = 0
        for x in range(26):
            if (x*determ)%26 == 1:
                multinv = x
        return multinv

    @staticmethod
    def inverzkljuc(invmat):
        detkljuc= Matrice.determinanta(invmat)
        invdet = Hill.multiverz(detkljuc)
        
        pomocni = []
        for x in range(len(invmat)):
            kofaktor = []
            for y in range(len(invmat)):
                minormat = Matrice.minor(invmat, x, y)
                kofaktor.append((((-1) ** (x+y))) * Matrice.determinanta(minormat))
                    
            pomocni.append(kofaktor)
        pomocni = list(Matrice.traninv(pomocni))
        zavrsni = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for x in range(3):
            for y in range(3):
                zavrsni[x][y] = (invdet * pomocni[x][y])%26
        return zavrsni
                

    @staticmethod
    def dekriptiranje(kljucfin, sifrat):
        kljucfin = Hill.inverzkljuc(kljucfin)
        pomocni = []
        privremeni = 0
        sifrato = ''
        print(kljucfin)
        print(sifrat)
        while len(sifrat) >= 0:
            if len(sifrat) == 0:
                break
            if len(sifrat) == 2:
                sifrat.append(0)
            elif len(sifrat) == 1:
                sifrat.append(0)
                sifrat.append(0)
            for x in range(3):
                privremeni = 0
                for y in range(3):
                    privremeni += kljucfin[x][y]*sifrat[y]
                pomocni.append(privremeni%26)
                print(pomocni)
            sifrat.reverse()
            sifrat.pop()
            sifrat.pop()
            sifrat.pop()
            sifrat.reverse()
        sifrato = ''.join(chr(round(slovo)+65) for slovo in pomocni)
        print(sifrato)
    


while True:
    
    print("\nDobrodošli u glavni izbornik!\n 1. Zbrajanje matrica\n 2. Oduzimanje matrice\n 3. Množenje sa skalarom\n 4. Množenje matrica\n 5. Transponiranje Matrice\n 6. Determinanta matrice\n 7. Inverz matrice\n 8. Hillova šifra (KRIPTIRANJE)\n 9. Hillova šifra (DEKRIPTIRANJE)")
    choice = int(input("\nUpiši redni broj da bi započeo željenu operaciju  "))
    
    
    match choice:
        case 1: 
            #Prva matrica
            print("#### ZBRAJANJE ####\n Upiši veličinu prve matrice (` 2 2 ` za matricu veličine 2 puta 2): ")
            matx = Matrice(input())
            print("Unesi prvu matricu (` 2 2 ` pa enter za sljedeci redak):")
            matx.novamat()
            #Druga matrica
            print("Upiši veličinu druge matrice: ")
            maty = Matrice(input())
            print("Unesi drugu matricu: ")
            maty.novamat()
            
            print("Rezultat je:")
            matx.zbrajanje(maty)  ##pozivanje funkcije
            
        
        case 2:
            #Prva matrica
            print("#### ODUZIMANJE ####\n Upiši veličinu prve matrice (` 2 2 ` za matricu veličine 2 puta 2): ")
            matx = Matrice(input())
            print("Unesi prvu matricu (` 2 2 ` pa enter za sljedeci redak):")
            matx.novamat()
            #Druga matrica
            print("Upiši veličinu druge matrice: ")
            maty = Matrice(input())
            print("Unesi drugu matricu: ")
            maty.novamat()
            
            print("Rezultat je:")
            matx.oduzimanje(maty)  ##pozivanje funkcije
            
        
        case 3:
            print("#### MNOŽENJE MATRICE SA SKALAROM ####\n Upiši veličinu matrice koju hočeš pomnožiti (` 2 2 ` za matricu veličine 2 puta 2): ")
            matx = Matrice(input())
            print("Unesi matricu (` 2 2 ` pa enter za sljedeci redak):")
            matx.novamat()
            #unos skalara
            print("Unesi skalar po izboru: ")
            skal = float(input())
            
            print("Rezultat je:")
            matx.skalar(skal)
            
        
        case 4:
            #Prva matrica
            print("#### MNOŽENJE MATRICA ####\n Upiši veličinu prve matrice koju hočeš pomnožiti (` 2 2 ` za matricu veličine 2 puta 2): ")
            matx = Matrice(input())
            print("Unesi prvu matricu (` 2 2 ` pa enter za sljedeci redak):")
            matx.novamat()
            #Druga matrica
            print("Upiši veličinu druge matrice: ")
            maty = Matrice(input())
            print("Unesi drugu matricu: ")
            maty.novamat()
            
            print("Rezultat je:")
            matx.mnozenje(maty)
            
        
        case 5:
            print("#### TRANSPONIRANJE MATRICE ####\n Upiši veličinu matrice koju hočeš transponirati (` 2 2 ` za matricu veličine 2 puta 2): ")
            matx = Matrice(input())
            print("Unesi matricu: ")
            matx.novamat()
            #Pozivanje funkcije za transponiranje
            print("Transponirana matrica je: ")
            matx.transponiranje()
        
        case 6:
            print("#### PRONALAŽENJE DETERMINANTE ####\n Upiši veličinu matrice od koje hočeš naći determinantu, matrica mora biti kvadratna (` 2 2 ` za matricu veličine 2 puta 2): ")
            matx = Matrice(input())
            print("Unesi matricu: ")
            matx.novamat()
            #Pozivanje funkcije za determinantu
            print("Determinanta tražene matrice: ")
            print(matx.determinanta(matx.matrica))
        
        case 7:
            print("#### INVERZ MATRICE ####\n Upiši veličinu matrice od koje hočeš naći determinantu, matrica mora biti kvadratna (` 2 2 ` za matricu veličine 2 puta 2): ")
            matx = Matrice(input())
            print("Unesi matricu: ")
            matx.novamat()
            
            print("Inverz matrica je: ")
            Matrice.inverz(matx.matrica)
            
        case 8:
            print("#### HILLOVA ŠIFRA / KODER ####\n Ključ mora biti kvadratna matrica duljine 3 puta 3")
            print("Unesi ključ: ")
            kljuc = []
            kljuc = Hill.novikljuc(kljuc)
            print(kljuc)
            print(Matrice.determinanta(kljuc))
            if Matrice.determinanta(kljuc) != 0:
                print("determinanta nije 0")
                if Matrice.determinanta(kljuc)%2!=0:
                    print("determinanta nije modulo 2")
                    if Matrice.determinanta(kljuc)%13!=0:
                        print("determinanta nije modulo 13")
                        rijec = str(input("Daj mi riječ: "))
                        rijec = Hill.rastav(rijec)
                        Hill.kriptiranje(kljuc, rijec)
            else:
                print("Ključ ne zadovoljava uvjete! Determinanta ")
        
        case 9:
            print("#### HILLOVA ŠIFRA / DEKODER ####\n Ključ mora biti kvadratna matrica duljine 3 puta 3")
            print("Unesi ključ: ")
            kljuc = []
            kljuc = Hill.novikljuc(kljuc)
            print(kljuc)
            print(Matrice.determinanta(kljuc))
            if Matrice.determinanta(kljuc) != 0:
                print("determinanta nije 0")
                if Matrice.determinanta(kljuc)%2!=0:
                    print("determinanta nije modulo 2")
                    if Matrice.determinanta(kljuc)%13!=0:
                        print("determinanta nije modulo 13")
                        sifra = str(input("Daj mi šifrat: "))
                        sifra = Hill.rastav(sifra)
                        Hill.dekriptiranje(kljuc, sifra)
                    else:
                        print("Ključ ne zadovoljava uvjete!")
                else:
                    print("Ključ ne zadovoljava uvjete!")
            else:
                print("Ključ ne zadovoljava uvjete! Determinanta ")