FROM Sibu07/hk-updated:latest
WORKDIR /usr/src/app
COPY . .
CMD ["bash", "start.sh"]
