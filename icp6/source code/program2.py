# importing pandas package and sklearn
import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# reading the csv from storage
variables = pandas.read_csv('sample_stocks.csv')

# assigning the returns coulmn to variable X from the csv file
Y = variables[['returns']]

# assigning the dividendyield coulmn to variable X from the csv file
X = variables[['dividendyield']]

Nc = range(1, 20)

# forming the clusters
kmeans = [KMeans(n_clusters=i) for i in Nc]

score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]

pl.plot(Nc,score)

pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')

# plotting the elbow curve
pl.show()
pca = PCA(n_components=1).fit(Y)
pca_d = pca.transform(Y)
pca_c = pca.transform(X)

# declared the number of clusters for 3
kmeans=KMeans(n_clusters=3)
kmeansoutput=kmeans.fit(Y)

pl.figure('3 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
pl.show()