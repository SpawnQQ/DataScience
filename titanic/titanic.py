#Primer par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Pclass")
plt.xlabel("Pclass")
plt.ylabel("Survived")

plt.hist([df[df['Survived']>0]['Pclass'],df[df['Survived']==0]['Pclass']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.title("Survived vs Sex")
plt.xlabel("Sex")
plt.ylabel("Survived")

plt.hist([df[df['Survived']>0]['Sex'],df[df['Survived']==0]['Sex']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])
plt.show()

#Segundo par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Age")
plt.xlabel("Age")
plt.ylabel("Survived")

plt.hist([df[df['Survived']>0]['Age'],df[df['Survived']==0]['Age']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.title("Survived vs SibSp")
plt.xlabel("SibSp")
plt.ylabel("Survived")

plt.hist([df[df['Survived']>0]['SibSp'],df[df['Survived']==0]['SibSp']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])
plt.show()

#Tercer par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Parch")
plt.xlabel("Parch")
plt.ylabel("Survived")

plt.hist([df[df['Survived']>0]['Parch'],df[df['Survived']==0]['Parch']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.title("Survived vs Fare")
plt.xlabel("Fare")
plt.ylabel("Survived")

plt.hist([df[df['Survived']>0]['Fare'],df[df['Survived']==0]['Fare']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])
plt.show()

#Cuarto par de graficos

plt.figure(figsize=(15, 4), dpi=70)
plt.subplot(1,2,1)
plt.title("Survived vs Embarked")
plt.xlabel("Embarked")
plt.ylabel("Survived")

plt.hist([df[df['Survived']>0]['Embarked'],df[df['Survived']==0]['Embarked']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Not survive','Survived'])

plt.subplot(1,2,2)
plt.show()