import seaborn as sns
planets = sns.load_dataset("planets")
df= planets.copy()
print(df.head())

df_num= df.select_dtypes(include = ["float64","int64"])# sayısal değişkenleri seçiyoruz
print(df_num.head().T)

print(df_num["distance"].describe().T)# distance değişkeninin istatistiksel bilgilerini verir