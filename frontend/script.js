
const API = "http://127.0.0.1:8000/categoria";

// LISTAR CATEGORIAS
async function listarCategorias() {

    const resposta = await fetch(API);

    const categorias = await resposta.json();

    const tabela = document.getElementById("listaCategorias");

    tabela.innerHTML = "";

    categorias.forEach(categoria => {

        tabela.innerHTML += `
            <tr>
                <td>${categoria.id_categoria}</td>

                <td>${categoria.nome_categoria}</td>

                <td>
                    <button class="btn-editar"
                        onclick="editarCategoria(${categoria.id_categoria}, '${categoria.nome_categoria}')">
                        Editar
                    </button>

                    <button class="btn-excluir"
                        onclick="excluirCategoria(${categoria.id_categoria})">
                        Excluir
                    </button>
                </td>
            </tr>
        `;
    });
}


// CADASTRAR CATEGORIA
document.getElementById("formCategoria")
.addEventListener("submit", async function(event) {

    event.preventDefault();

    const nome = document.getElementById("nome_categoria").value;

    const resposta = await fetch(API, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            nome_categoria: nome
        })
    });

    if (!resposta.ok) {
        alert("Erro ao cadastrar categoria!");
        return;
    }

    alert("Categoria cadastrada com sucesso!");

    document.getElementById("formCategoria").reset();

    listarCategorias();
});


// EDITAR CATEGORIA
async function editarCategoria(id, nomeAtual) {

    const novoNome = prompt("Digite o novo nome:", nomeAtual);

    if (!novoNome || !novoNome.trim()) {
        return;
    }

    const resposta = await fetch(`${API}/${id}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            nome_categoria: novoNome.trim()
        })
    });

    if (!resposta.ok) {
        alert("Erro ao atualizar categoria!");
        return;
    }

    alert("Categoria atualizada!");

    listarCategorias();
}


// EXCLUIR CATEGORIA
async function excluirCategoria(id) {

    if (!confirm("Deseja realmente excluir esta categoria?")) {
        return;
    }

    const resposta = await fetch(`${API}/${id}`, {
        method: "DELETE"
    });

    if (!resposta.ok) {
        alert("Erro ao excluir categoria!");
        return;
    }

    alert("Categoria excluída!");

    listarCategorias();
}


// CARREGAR CATEGORIAS AO ABRIR A PÁGINA
listarCategorias();
