# EECS 485: Project 5

### Reminders
  - Make sure it works on CAEN
  - Make sure you download the starter files from the public Google Drive. Some of the files in there are gitignore'd by their given gitignore.

### Group Name: Raynor's Raiders

### Final Exam
	main problem in consistency models:
	to keep things consisten between users, remember that different messages take different amounts of time to send

### Members
  - John West (johnwest) - Protoss
    - yolo swag
  - Diego Calvo (calvod) - Zerg
    - yolo swag
  - Nick Cruz (ncruz) - Zerg
    - yolo swag

### Installation
Make sure you have all requirements installed (should only need to do this once). While in vagrant, in the root directory:
```
sudo pip install -r requirements.txt
sudo pip install -r flask/requirements.txt
sudo pip install requests
```

### Part 1: MapReduce Indexing

### Part 2: Integrated Ranking

##### Python script for mining.edges.xml
The python script that converts `mining.edges.xml` to `pagerank.net` (Pajek format) is `pagerank/edges.py`.
To run, make sure you are in `pagerank/` and type:
```
python edges.py > pagerank_code/pagerank.net
```

### Part 3: The New Search Interface

### Custom makefile commands
To run the C++ server, type this while in `index_server/`:
```
make rebuild
```

### Extra:
  - zerg4lyfe
