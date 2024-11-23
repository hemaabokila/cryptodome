
let libraries = {};

document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:8000/python/api/libraries/')
        .then(response => response.json())
        .then(data => {
            console.log(data); 
            libraries = data.reduce((acc, library) => {
                acc[library.name.toLowerCase()] = library;
                return acc;
            }, {});

            const listGroup = document.getElementById('library-list');
            Object.keys(libraries).forEach((key) => {
                const library = libraries[key];
                const listItem = document.createElement('li');
                listItem.className = 'list-group-item';
                listItem.id = `library-${key}`;
                listItem.textContent = library.name;
                listItem.onclick = () => showLibrary(key);
                listGroup.appendChild(listItem);
            });
            showLibrary('numpy');
        })
        .catch((error) => {
            console.error('Error fetching libraries data:', error);
        });
});

function showLibrary(libraryKey) {
    const library = libraries[libraryKey];
    if (!library) return;
    const libraryInfo = document.getElementById('library-info');
    const libraryName = document.getElementById('library-name');
    const libraryExample = document.getElementById('library-example');
    const libraryInstall = document.getElementById('library-install');
    const libraryDescription = document.getElementById('library-description');

    libraryName.textContent = library.name;
    libraryExample.textContent = library.example;
    libraryInstall.querySelector('code').textContent = library.install;
    libraryDescription.textContent = library.description;
    libraryInfo.classList.remove('d-none');
    document.querySelectorAll('.list-group-item').forEach((item) => {
        item.classList.remove('active');
    });
    document.getElementById(`library-${libraryKey}`).classList.add('active');
    Prism.highlightAll();
}

let codes = {};  
document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:8000/python/api/codes/')
        .then(response => response.json())
        .then(data => {
            console.log(data); 
            codes = data.reduce((acc, code) => {
                acc[code.name.toLowerCase()] = code;
                return acc;
            }, {});
            const listGroup = document.getElementById('code-list');
            Object.keys(codes).forEach((key) => {
                const code = codes[key];
                const listItem = document.createElement('li');
                listItem.className = 'list-group-item';
                listItem.id = `code-${key}`;
                listItem.textContent = code.name;
                listItem.onclick = () => showCode(key);
                listGroup.appendChild(listItem);
            });

            showCode('admin panel finder');
        })
        .catch((error) => {
            console.error('Error fetching codes data:', error);
        });
});

function showCode(codeKey) {
    const code = codes[codeKey];
    if (!code) return;
    const codeInfo = document.getElementById('code-info');
    const codeName = document.getElementById('code-name');
    const codeExample = document.getElementById('code-example');
    const codeInstall = document.getElementById('code-install');
    const codeDescription = document.getElementById('code-description');
    const codeUrl = document.getElementById('code-url');
    codeUrl.href = code.url || "#";     
    codeInfo.classList.remove('d-none');

    codeName.textContent = code.name;
    codeExample.textContent = code.example;
    codeInstall.querySelector('code').textContent = code.install;
    codeDescription.textContent = code.description;
    codeInfo.classList.remove('d-none');
    document.querySelectorAll('.list-group-item').forEach((item) => {
        item.classList.remove('active');
    });
    document.getElementById(`code-${codeKey}`).classList.add('active');
    Prism.highlightAll();
}

const counters = document.querySelectorAll('.counter');

counters.forEach(counter => {
    counter.innerText = '0'; 

    const updateCounter = () => {
        const target = +counter.getAttribute('data-count');
        const current = +counter.innerText;
        const increment = target / 100;

        if (current < target) {
            counter.innerText = Math.ceil(current + increment);
            setTimeout(updateCounter, 1);
        } else {
            counter.innerText = target;
        }
    };

    updateCounter();
});
