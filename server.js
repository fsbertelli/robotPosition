const http = require('http');

const url = 'http://espia:strongpiopio042@52.161.96.125:3001/robot.log?1046';

http.get(url, (response) => {
  let data = '';

  response.on('data', (chunk) => {
    data += chunk;
  });

  response.on('end', () => {
    if (response.statusCode === 200) {
      // Aqui, data contém a resposta do servidor em formato de texto
      console.log(data);
    } else {
      console.log(`Erro: ${response.statusCode}`);
    }
  });
}).on('error', (error) => {
  console.error(`Erro na solicitação: ${error.message}`);
});
