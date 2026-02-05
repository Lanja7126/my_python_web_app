# Intégration manuel

### 1 Se connecter à notre compte:
```bash
  docker login -u your_docekr_login
```

### 2 Lister tous les images:

```bash
  docker images
```

### 3 Construire un image à partir d'un projet:

```bash
  docker build -t your_docker_login/your_project_name:your_tag(default : latest)
```

### 4 Taguer l'image docker:

```bash
  docekr tag your_docker_login/your_project_name:your_tag(default : latest)
```

### 5 Envoyer l'image dans dockerhub:

```bash
  docker push your_docker_login/your_project_name
```
