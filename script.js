async function buscarUsuarios() {

  const resposta = await fetch(
    "https://jsonplaceholder.typicode.com/users"
  );

  const usuarios = await resposta.json();

  const lista = document.getElementById(
    "listaUsuarios"
  );

  lista.innerHTML = "";

  usuarios.forEach(usuario => {
    lista.innerHTML += `
      <li>
        ${usuario.name}
        ${usuario.email}
        ${usuario.address.zipcode}
      </li>
    `;
  });
}