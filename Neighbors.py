from sklearn.neighbors import NearestCentroid

# Dtabase : Gerbang logika AND
# x = Data, y = Target
x = [[0,0], [0,1], [1,0], [1,1], [0,2], [1,2], [2,0], [2,1], [2,2], [0,3]]
y = [0,0,0,1,0,0,0,0,1,0]

# Traininy and Classify
clf = NearestCentroid()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Nearest Neighbots")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("0 2 =", clf.predict([[0,2]]))
print ("1 2=", clf.predict([[1, 2]]))
print ("2 0 =", clf.predict([[2,0]]))
print ("2 1 =", clf.predict([[2,1]]))
print ("2 2=", clf.predict([[2,2]]))
print ("0 3 =", clf.predict([[0,3]]))