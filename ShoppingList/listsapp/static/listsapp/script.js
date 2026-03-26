document.addEventListener("DOMContentLoaded", () => {
    console.log("1. A página carregou. Procurando os botões...");

    const addBtn = document.getElementById("add-address-btn");
    const editBtn = document.getElementById("edit-address-btn");

    if (addBtn) {
        addBtn.onclick = (e) => {
            e.preventDefault(); 
            showAddressForm();
        };
    }

    if (editBtn) {
        editBtn.onclick = (e) => {
            e.preventDefault();
            showAddressForm();
        };
    }
});

function showAddressForm() {
    const container = document.getElementById("address-container");
    // Pega o endereço atual (se existir) para já preencher o input
    const currentAddress = document.getElementById("address-text") ? 
        document.getElementById("address-text").innerText.replace('Address: ', '').trim() : '';

    container.innerHTML = `
        <div class="card border-dashed p-3 bg-light shadow-sm w-100">
            <div class="input-group">
                <input id="address-input" type="text" class="form-control" placeholder="Street, Number..." value="${currentAddress}" required>
                <button class="btn btn-primary" onclick="saveAddress()">
                    Save
                </button>
            </div>
        </div>
    `;
    // Foca no input automaticamente
    document.getElementById("address-input").focus();
}

function saveAddress() {
    const container = document.getElementById("address-container");
    const address = document.getElementById("address-input").value;
    const supermarketId = container.getAttribute("data-supermarket-id"); // Pega o ID dinâmico

    // Ajuste a URL caso no seu urls.py ela seja diferente!
    fetch(`/update_address/${supermarketId}/`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ address: address })
    })
    .then(response => {
        if (!response.ok) throw new Error("Erro de autorização ou servidor");
        return response.json();
    })
    .then(data => {
        // Reconstrói a visualização do endereço
        container.innerHTML = `
            <div class="bg-light p-3 rounded-pill border shadow-sm px-4 d-flex justify-content-between align-items-center">
                <span id="address-text" class="text-muted">
                    <i class="bi bi-geo-alt-fill text-danger me-1"></i> 
                    <strong>Address:</strong> ${data.address}
                </span>

                <button class="btn btn-sm btn-outline-secondary ms-3" id="edit-address-btn">
                    Edit
                </button>
            </div>
        `;
        // Religa o evento de clique no botão recém-criado
        document.getElementById("edit-address-btn").onclick = showAddressForm;
    })
    .catch(error => {
        alert("Erro ao salvar endereço. Tente novamente.");
        console.error(error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("click", function(e) {
        // Verifica se clicou em um link de paginação
        if (e.target.classList.contains("page-link")) {
            e.preventDefault();
            const url = e.target.href;
            
            if (!url) return;

            // Faz a requisição AJAX
            fetch(url, {
                headers: { "X-Requested-With": "XMLHttpRequest" }
            })
            .then(response => response.json())
            .then(data => {
                // Atualiza apenas o container de produtos
                document.getElementById("product-container").innerHTML = data.html;
                // Move o scroll para o topo suavemente
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
    });