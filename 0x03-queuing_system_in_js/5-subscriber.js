const client = require('./5-publisher');

// const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`);
})

client.on('connect', () => console.log('Redis client connected to the server'));

client.subscribe("holberton school channel");

function killServer() {
    client.unsubscribe('holberton school channel');
    client.QUIT();
}

client.on('message', (channel, message) => {
    if (message === "KILL_SERVER") {
        killServer();
    }
    console.log(message);
})
