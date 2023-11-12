import seaborn as sns
planets = sns.load_dataset("planets")
print("Veri setinin ilk 5 Satırı:",planets.head())# ilk beş satırı yazdırıyoruz

print("veri setinin son beş satırı:",planets.tail())# son beş satırı yazdırıyoruz

df=planets.copy()# veri setini kopyalıyoruz birnevi yedeğini almış oluyoruz

print(df.head())

print("---------------Veri seti nin yapısı------------------")
#veri seti yapısını öğrenmek için
print(df.info())


print(df.describe())# sadece sayısal değişkenlerin istatistiksel bilgilerini verir
import pandas as pd
df.method = pd.Categorical(df.method)# method değişkenini kategorik değişken olarak tanımlıyoruz
print(df.head())
print(df.shape)# veri setinin boyutunu verir    (row,column)

print("---------------Veri seti nin transpozu------------------")
print(df.describe().T)# transpozunu alıyoruz    (row,column) yer değiştiriyoruz.

print("*********Metod değişkenindeki değerlerin kaçtane olduğu************ .")
print(df["method"].value_counts())# method değişkenindeki değerlerin kaçar tane olduğunu gösteriyor.

print(df.isnull().sum())# veri setinde eksik değer var mı yok mu onu gösteriyor



#veri seti içersinde eksik değerleri ortalama ile doldurma işlemi kodu
print(df["orbital_period"].fillna(df["orbital_period"].mean(),inplace=True))# orbital_period değişkenindeki eksik değerleri ortalama ile dolduruyoruz
print(df.head())

print(df["mass"].fillna(df["mass"].mean(),inplace=True))# mass değişkenindeki eksik değerleri ortalama ile dolduruyoruz
print(df.head())

print("/////////////////////////////////////////////////////////////////")
import pandas as pd
df.method = pd.Categorical(df.method)# method değişkenini kategorik değişken olarak tanımlıyoruz
print(df.head())
print(df.shape)# veri setinin boyutunu verir    (row,column)
kat_df = df.select_dtypes(include = ["category"])# kategorik değişkenleri seçiyoruz
print(kat_df.method.value_counts())# method değişkenindeki değerlerin kaçar tane olduğunu gösteriyor.
print(kat_df.info())# kategorik değişkenlerin bilgilerini verir
print(kat_df["method"].value_counts())# method değişkenindeki değerlerin kaçar tane olduğunu gösteriyor.

#veri setindeki değerlerin grafik olarak gösterilmesi veri görselleştirme
counts = df["method"].value_counts()
plot = counts.plot.barh()
print(plot)


