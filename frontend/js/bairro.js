async function carregarBairros() {
    const lista = document.getElementById("lista-bairros");
    lista.textContent = "Carregando...";

    try {
        const resposta = await fetch("/bairros");

        if (!resposta.ok) {
            throw new Error(`Erro ao buscar bairros: ${resposta.status}`);
        }

        const bairros = await resposta.json();
        lista.replaceChildren();

        if (bairros.length === 0) {
            lista.textContent = "Nenhum bairro cadastrado.";
            return;
        }

        bairros.forEach((bairro) => {
            const item = document.createElement("li");

            item.textContent =
                `${bairro.nome_bairro} — ${bairro.cidade}/${bairro.estado}`;

            lista.appendChild(item);
        });
    } catch (erro) {
        lista.textContent = "Não foi possível carregar os bairros.";
        console.error(erro);
    }
}

carregarBairros();