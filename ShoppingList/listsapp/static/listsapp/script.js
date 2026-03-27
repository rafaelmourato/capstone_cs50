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
    document.getElementById("address-input").focus();
}

function saveAddress() {
    const container = document.getElementById("address-container");
    const address = document.getElementById("address-input").value;
    const supermarketId = container.getAttribute("data-supermarket-id"); 
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
        container.innerHTML = `
            <div class="bg-light p-3 rounded-pill border shadow-sm px-4 d-flex justify-content-between align-items-center">
                <span id="address-text" class="text-muted">
                    <i class="bi bi-geo-alt-fill text-danger me-1"></i> 
                    <strong>Address:</strong> ${data.address}  
                </span>

                <button class="btn btn-sm ml-2 btn-outline-secondary ms-3" id="edit-address-btn">
                    Edit
                </button>
            </div>
        `;
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
    if (e.target.classList.contains("page-link")) {
        e.preventDefault();
        const url = e.target.href;
        if (!url) return;
        fetch(url, {
            headers: { "X-Requested-With": "XMLHttpRequest" }
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("product-container").innerHTML = data.html;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("create-list-form");
    
    if (form) {
        form.onsubmit = function(e) {
            e.preventDefault(); 
            const nameInput = document.getElementById("new-list-name");
            const formData = new FormData();
            formData.append("listname", nameInput.value);
            formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
            fetch("{% url 'userpage' %}", {
                method: "POST",
                body: formData,
                headers: { "X-Requested-With": "XMLHttpRequest" }
            })
            .then(r => r.json())
            .then(data => {
                const emptyMsg = document.getElementById("empty-msg");
                if (emptyMsg) emptyMsg.remove();
                const newCard = `
                    <div class="col-md-4 mb-3" id="list-card-${data.id}">
                        <div class="card h-100 border-0 shadow-sm transition">
                            <div class="card-body">
                                <h5 class="fw-bold mb-3">${data.name}</h5>
                                <a href="${data.url}" class="btn btn-outline-primary btn-sm rounded-pill w-100">Open List</a>
                            </div>
                        </div>
                    </div>`;
                
                document.getElementById("lists-wrapper").insertAdjacentHTML('afterbegin', newCard);
                nameInput.value = ""; 
            })
            .catch(error => console.error("Erro no Fetch:", error));
        };
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const listForm = document.getElementById("add-product-to-list-form"); // Novo ID
    const productSelect = document.getElementById("product-select");
    const productList = document.getElementById("product-list");

    if (listForm) {
        listForm.onsubmit = function(e) {
            e.preventDefault();
            const productId = productSelect.value;
            if (!productId) return;

            const formData = new FormData();
            formData.append("product_id", productId);
            formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));

            fetch(window.location.href, {
                method: "POST",
                body: formData,
                headers: { "X-Requested-With": "XMLHttpRequest" }
            })
            .then(r => r.json())
            .then(data => {
                if (data.success) {
                    const emptyMsg = document.getElementById("empty-msg");
                    if (emptyMsg) emptyMsg.remove();
                    
                    const newItem = `
                        <div class="list-group-item d-flex align-items-center py-3 border-bottom animate__animated animate__fadeIn">
                            <i class="bi bi-circle me-3 text-muted"></i>
                            <span class="fw-bold">${data.name}</span>
                            <span class="text-muted ms-2 small">(${data.unity || ''})</span>
                        </div>`;
                    
                    productList.insertAdjacentHTML('afterbegin', newItem);
                    
                    const optionToRemove = productSelect.querySelector(`option[value="${productId}"]`);
                    if (optionToRemove) optionToRemove.remove();
                    listForm.reset();
                }
            })
            .catch(error => console.error("Error adding to list:", error));
        };
    }
});

// --- FUNÇÃO PARA A PÁGINA DE SUPERMERCADO (supermarketpage) ---
document.addEventListener("DOMContentLoaded", () => {
    const mktForm = document.getElementById("add-product-form"); // Mantém o ID original
    const productSelect = document.getElementById("product-select");
    const productList = document.getElementById("product-list");

    if (mktForm) {
        mktForm.onsubmit = function(e) {
            e.preventDefault();
            const productId = productSelect.value;
            const priceInput = mktForm.querySelector('input[name="price"]');
            
            if (!productId || !priceInput || !priceInput.value) return;

            const formData = new FormData();
            formData.append("product_id", productId);
            formData.append("price", priceInput.value);
            formData.append("action", "add_product"); 
            formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));

            fetch(window.location.href, {
                method: "POST",
                body: formData,
                headers: { "X-Requested-With": "XMLHttpRequest" }
            })
            .then(r => r.json())
            .then(data => {
                if (data.success) {
                    const emptyMsg = document.getElementById("no-products-msg");
                    if (emptyMsg) emptyMsg.remove();
                    
                    const img = data.picture_url 
                        ? `<img src="${data.picture_url}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 8px;">`
                        : `<div style="width: 60px; height: 60px; background: #eee; border-radius: 8px; display: flex; align-items: center; justify-content: center;">📦</div>`;
                    
                    const newItem = `
                        <div class="product-card border-bottom py-3 d-flex align-items-center">
                            <div class="me-3 ml-2">${img}</div>
                            <div class="flex-grow-1">
                                <h6 class="mb-1 ml-2">${data.name}</h6>
                                <small class="text-muted ml-2">$${data.price}</small>
                            </div>
                        </div>`; 
                    
                    productList.insertAdjacentHTML('afterbegin', newItem);
                    const optionToRemove = productSelect.querySelector(`option[value="${productId}"]`);
                    if (optionToRemove) optionToRemove.remove();
                    mktForm.reset();
                }
            })
            .catch(error => console.error("Error adding to market:", error));
        };
    }
});