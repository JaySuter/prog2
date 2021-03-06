# prog2

## ToDo-Liste "What's on your Mind?"


### Ausgangslage

Eine **ToDo-Liste** ist der Klassiker, um Dinge produktiver zu erledigen und nicht zu vergessen. Solche Listen helfen Ordnung im Chaos zu schaffen, erleichtern das Erinnern und verhindern bestenfalls das «Vor sich herschieben». Zudem machen sie Spass, und motivieren, wenn nach und nach Aufträge von der Liste gestrichen werden können. 

ToDo-Listen, die früher ausschliesslich mit Papier und Stift erstellt wurden, können heute mithilfe zahlreicher Apps bequem auf dem PC, Ipad oder Smartphone erfasst werden und sind so jederzeit abrufbereit. 

**_Haken an der ganzen Sache?_**
Will man eine vollumfängliche Applikation, die auf die eigenen Bedürfnisse angepasst ist und auch noch eine schöne Benutzeroberfläche hat, wird meist Geld gefordert. 

Mit meiner Web-Applikation **«What’s on your mind?»** habe ich mir Grundlagen zum Programmieren einer Applikation angeeignet und eine simple ToDo-Listen konstruiert. 



### Funktion / Projektidee  

Die Applikation ist zur einfachen Erstellung von Aufgaben-Listen fähig. Das Selbstmanagement-Tool dient folglich als Plattform, Aufgaben zu sammeln und nach erfolgreicher Durchführung auf eine Liste mit den erledigten Tasks zu verschieben. 
Des Weiteren gibt die Plattform an, wieviele der aufgeführten Tasks bereits erledigt, oder noch zu tun sind. Erledigte Tasks können auch wieder zurück auf die Hauptseite der noch offenen Task verschoben oder gelöscht werden. 



### Workflow

##### Task erstellen, speichern und als erledigt markieren 
  ![flowchart](https://user-images.githubusercontent.com/55581677/72160268-53be3a80-33be-11ea-9975-a31ec29f4a05.png)


* #### Dateneingabe
  *	Erstellen verschiedener Aufgaben / Tasks 


* #### Datenverarbeitung / Speicherung
  *	Speichern der erstellten Tasks (submit)
  * Ein erledigter Task mit "Done" markieren --> Wird auf Done-Liste verschoben.
  * Erledigte Tasks, die auf die "Done"-Liste verschoben wurden, können auch ganz gelöscht werden. 
  * Berechnung des Prozentsatzes wieviele Tasks schon erledigt sind, oder noch zu erledigen sind. 
  
  
* #### Datenausgabe 
  *	Erstellter Task anzeigen 
  * Prozentanzahl der zu erledigen Tasks und der erledigten Tasks anzeigen. 

 
 
 ### Benutzeranleitung 
 
 Die Webappliaktion ist bewusst sehr schlicht gehalten und ganz einfach zu bedienen:  
 
 1. Der Nutzer kann im Text-Feld sein Task erfassen und speichern (Submit) 
 
    ![todo_1](https://user-images.githubusercontent.com/55581677/72162226-d5639780-33c1-11ea-9651-ebf4e52a9b3c.jpg)
 
 
 2. Drückt der Nutzer auf "Submit" wird der Task unterhalb des Text- / Eingabefeldes aufgelistet. 
 
    ![todo_2](https://user-images.githubusercontent.com/55581677/72163305-e31a1c80-33c3-11ea-9161-d6d599ccf052.jpg)
 
 
 3. Mithilfe eines Counters wird dem Nutzer die Anzahl offenen Tasks und erledigten Tasks angezeigt.
 
    ![todo_3](https://user-images.githubusercontent.com/55581677/72162363-207daa80-33c2-11ea-8064-f4c03db9cfeb.jpg)
    
 
 4. Hat der Nutzer einen Task erledigt und drückt auf "Done" wird der Task auf die Done-Liste verschoben. 
    Die Done-Liste kann oben durch den Navigationsbutton "Done" aufgerufen werden. 
    
    ![todo_4](https://user-images.githubusercontent.com/55581677/72376499-572f2a00-370e-11ea-8078-3cb4a753b6c1.jpg)
    
    
 5. Will der Nutzer einen Task von der Done-Liste zurück zur ToDo-Liste verschieben, kann er ganz einfach den Button "Mark as 
    undone" drücken und der Task erscheint wieder auf der Open-Liste. 
    
    ![todo_5](https://user-images.githubusercontent.com/55581677/72162629-9aae2f00-33c2-11ea-9157-a5803a19236b.jpg)
    
    
 6. Will der Nutzer einen Task von der Done-Liste löschen, kann er den "Delete"-Button klicken und der Task wird
    unwiderruflich von der ToDo-Liste gelöscht. 
    
    ![todo_6](https://user-images.githubusercontent.com/55581677/72376566-6f06ae00-370e-11ea-8ecc-db402f30a564.jpg)

    
    
    
    
    
 
 
