from sklearn import tree

#DataSet

# features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
# labels = ["apple", "apple", "orange", "orange"]
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0,0,1,1]


#Train Clasifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[150, 0]])
