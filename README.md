# Flask Proto

Python Flask app with SQLite database running in Docker container for rapid API prototyping.

# Setup

1. Install [Docker](https://docs.docker.com/).
2. Navigate to this project folder in Terminal and run `docker-compose up`.
3. Open [localhost:5000](http://localhost:5000/) in browser and start hacking.

# Notes

- Flask runs in development mode and it will auto reload on file changes.
- Use `requirements.txt` to install additional Python libraries.
- Run `docker exec -it flask-proto bash` to get into Docker container.
- Run `docker start|stop|logs -f flask-proto` to control Docker container and see log.
