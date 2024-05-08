## Gerenciamento de Containers
- **`docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`**: Inicia um novo container com a imagem especificada.
- **`docker ps [OPTIONS]`**: Lista os containers em execução. Use `-a` para listar todos os containers (ativos e inativos).
- **`docker stop CONTAINER_ID/NAME`**: Para um container que está em execução.
- **`docker start CONTAINER_ID/NAME`**: Inicia um container que está parado.
- **`docker restart CONTAINER_ID/NAME`**: Reinicia um container.
- **`docker rm CONTAINER_ID/NAME`**: Remove um container. Use `-f` para forçar a remoção de um container em execução.
- **`docker logs CONTAINER_ID/NAME`**: Exibe os logs de um container.

## Gerenciamento de Imagens
- **`docker images`**: Lista todas as imagens locais.
- **`docker pull IMAGE_NAME:TAG`**: Baixa uma imagem do Docker Hub.
- **`docker rmi IMAGE_ID/NAME`**: Remove uma imagem local.
- **`docker build -t TAG [CONTEXT]`**: Constrói uma imagem a partir de um Dockerfile. `CONTEXT` é o diretório que contém o Dockerfile.

## Redes
- **`docker network ls`**: Lista as redes Docker.
- **`docker network create [OPTIONS] NETWORK`**: Cria uma nova rede.
- **`docker network rm NETWORK`**: Remove uma rede Docker.

## Volumes
- **`docker volume ls`**: Lista os volumes criados.
- **`docker volume create VOLUME_NAME`**: Cria um novo volume.
- **`docker volume rm VOLUME_NAME`**: Remove um volume.

## Gerenciamento de Docker Compose
- **`docker compose up [OPTIONS]`**: Inicia e anexa a todos os serviços definidos no arquivo `docker-compose.yml`.
- **`docker compose down`**: Para e remove os recursos (containers, redes, volumes) definidos no arquivo `docker-compose.yml`.

## Informações e Configurações
- **`docker info`**: Mostra informações do sistema Docker, como número de containers, imagens, configuração do driver de armazenamento, etc.
- **`docker version`**: Exibe a versão do Docker instalada.
- **`docker inspect OBJECT_NAME/ID`**: Retorna informações detalhadas sobre um objeto (container, imagem, volume, rede).
