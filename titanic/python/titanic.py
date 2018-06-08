#Primer par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Pclass")
plt.xlabel("Pclass")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['Pclass'],df[df['Survived']==0]['Pclass']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.title("Survived vs Sex")
plt.xlabel("Sex")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['Sex'],df[df['Survived']==0]['Sex']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])
plt.show()

#Segundo par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Age")
plt.xlabel("Age")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['Age'],df[df['Survived']==0]['Age']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.title("Survived vs SibSp")
plt.xlabel("SibSp")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['SibSp'],df[df['Survived']==0]['SibSp']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])
plt.show()

#Tercer par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Parch")
plt.xlabel("Parch")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['Parch'],df[df['Survived']==0]['Parch']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.title("Survived vs Fare")
plt.xlabel("Fare")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['Fare'],df[df['Survived']==0]['Fare']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])
plt.show()

#Cuarto par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Embarked")
plt.xlabel("Embarked")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['Embarked'],df[df['Survived']==0]['Embarked']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.title("Survived vs Ticket")
plt.xlabel("Ticket")
plt.ylabel("Survived")

plt.hist([df[df['Survived']==1]['Ticket'],df[df['Survived']==0]['Ticket']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])
plt.show()

test_titanic['Age'] = test_titanic['Age'].replace(test_titanic[test_titanic.isnull()['Age'] == True][test_titanic['Sex']=='male']['Age'],test_titanic[test_titanic.isnull()['Age'] == False][test_titanic['Sex']=='male']['Age'].median())
test_titanic['Age'] = test_titanic['Age'].replace(test_titanic[test_titanic.isnull()['Age'] == True][test_titanic['Sex']=='female']['Age'],test_titanic[test_titanic.isnull()['Age'] == False][test_titanic['Sex']=='female']['Age'].median())