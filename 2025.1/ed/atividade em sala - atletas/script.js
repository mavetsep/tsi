let athletes = JSON.parse(localStorage.getItem('athletes')) || [];

function saveToLocalStorage() {
    localStorage.setItem('athletes', JSON.stringify(athletes));
}

function renderAthleteTable() {
    const tableBody = document.getElementById('athleteTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';
    
    const sortedAthletes = [...athletes].sort((a, b) => a.name.localeCompare(b.name));
    
    if (sortedAthletes.length === 0) {
        const row = tableBody.insertRow();
        const cell = row.insertCell(0);
        cell.colSpan = 6;
        cell.textContent = 'Nenhum atleta cadastrado ainda.';
        cell.style.textAlign = 'center';
        return;
    }
    
    sortedAthletes.forEach(athlete => {
        const row = tableBody.insertRow();
        
        row.insertCell(0).textContent = athlete.name;
        row.insertCell(1).textContent = athlete.position;
        row.insertCell(2).textContent = athlete.height;
        row.insertCell(3).textContent = athlete.age;
        row.insertCell(4).textContent = athlete.city;
    });
}

function deleteAthlete(name) {
    if (confirm(`Tem certeza que deseja excluir o atleta ${name}?`)) {
        athletes = athletes.filter(athlete => athlete.name !== name);
        saveToLocalStorage();
        renderAthleteTable();
        alert('Atleta excluído com sucesso!');
    }
}

document.getElementById('athleteForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const newAthlete = {
        name: document.getElementById('name').value,
        position: document.getElementById('position').value,
        height: document.getElementById('height').value,
        age: document.getElementById('age').value,
        city: document.getElementById('city').value
    };
    
    const exists = athletes.some(a => a.name === newAthlete.name);
    if (exists) {
        alert('Já existe um atleta com esse nome!');
        return;
    }
    
    athletes.push(newAthlete);
    saveToLocalStorage();
    renderAthleteTable();
    
    this.reset();
    
    alert('Atleta cadastrado com sucesso!');
});

document.getElementById('searchBtn').addEventListener('click', function() {
    const searchName = document.getElementById('searchName').value.trim().toLowerCase();
    const resultDiv = document.getElementById('searchResult');
    
    if (!searchName) {
        resultDiv.innerHTML = '<p style="color: red;">Por favor, digite um nome para buscar.</p>';
        return;
    }
    
    const foundAthletes = athletes.filter(athlete => 
        athlete.name.toLowerCase().includes(searchName)
    );
    
    if (foundAthletes.length > 0) {
        let html = '<h3>Resultados da Busca:</h3><table><thead><tr><th>Nome</th><th>Posição</th><th>Altura</th><th>Idade</th><th>Cidade</th></tr></thead><tbody>';
        
        foundAthletes.forEach(athlete => {
            html += `
                <tr>
                    <td>${athlete.name}</td>
                    <td>${athlete.position}</td>
                    <td>${athlete.height} cm</td>
                    <td>${athlete.age} anos</td>
                    <td>${athlete.city}</td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        resultDiv.innerHTML = html;
    } else {
        resultDiv.innerHTML = '<p>Nenhum atleta encontrado com esse nome.</p>';
    }
});

document.getElementById('deleteBtn').addEventListener('click', function() {
    const searchName = document.getElementById('searchName').value.trim();
    const resultDiv = document.getElementById('searchResult');
    
    if (!searchName) {
        resultDiv.innerHTML = '<p style="color: red;">Por favor, digite um nome para excluir.</p>';
        return;
    }
    
    const initialLength = athletes.length;
    athletes = athletes.filter(athlete => 
        !athlete.name.toLowerCase().includes(searchName.toLowerCase())
    );
    
    if (athletes.length < initialLength) {
        saveToLocalStorage();
        renderAthleteTable();
        resultDiv.innerHTML = '<p style="color: green;">Atleta(s) removido(s) com sucesso!</p>';
    } else {
        resultDiv.innerHTML = '<p>Nenhum atleta encontrado com esse nome.</p>';
    }
});

renderAthleteTable();