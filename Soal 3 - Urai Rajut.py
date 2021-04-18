class urai_rajut:                                     #membuat class urai_rajut yang terdapat 2 fungsi
    
    def urai(self,kata) :                            #fungsi 1 : urai 
        hasil = ''                                   #variabel kosong untuk menampung iterasi dari loop
        for i in range (len(kata)+1):                #menghitung panjang kata - kata
            for j in range(i):                       
                hasil += kata[j]                     #variabel hasil akan ditambahkan oleh isi dari kata di index ke j, namun belum bisa reverse seperti di soal contoh 'CCoCodCodeCodCoC' atau 'PPyPytPythPythoPythonPythoPythPytPyP'
 
        return hasil                                 #return ke hasil
    
    def rajut(self,kata2):                               #funngsi 2 : rajut                            
        hitung_kata = len(kata2)                         #menghitung panjang kata - kata
        kapital = sum(1 for c in (kata2) if c.isupper()) #mencari huruf kapital menggunakan kondisi 'if'

        hapus = hitung_kata-kapital                    #untuk menghitung total huruf yang akan dihapus
                                                       
        hasil = kata2[hapus:hitung_kata]               
        return hasil                                   #return ke hasil
       

func = urai_rajut()                                     #Panggil kelas urai_rajut

#function urai
print(func.urai('Code'))                        
print(func.urai('Python'))
print(func.urai('Purwadhika'))
print('=================')
#funtion rajut
print(func.rajut('CCoCodCode'))
print(func.rajut('PPyPytPythPythoPython'))
print(func.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))



