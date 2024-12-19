// botones
const toastTrigger1 = document.getElementById('liveToastBtn1');
const toastTrigger2 = document.getElementById('liveToastBtn2');
const toastTrigger3 = document.getElementById('liveToastBtn3');
const toastTrigger4 = document.getElementById('liveToastBtn4');
const toastTrigger5 = document.getElementById('liveToastBtn5');
const toastTrigger6 = document.getElementById('liveToastBtn6');
// contenedor toast
const toastLiveExample1 = document.getElementById('liveToast1');
const toastLiveExample2 = document.getElementById('liveToast2');
const toastLiveExample3 = document.getElementById('liveToast3');
const toastLiveExample4 = document.getElementById('liveToast4');
const toastLiveExample5 = document.getElementById('liveToast5');
const toastLiveExample6 = document.getElementById('liveToast6');
// seccion plataformas
const sectionPlataforma = document.getElementById('plataformas');
const columna = document.getElementById('columna-4');
const columna5 = document.getElementById('columna-5');
const columna6 = document.getElementById('columna-6');
// mostrar iframe modulos de cotizacion
const boton_cotizacion = document.getElementById('boton_cotizacion');
const iframe_cotizacion = document.getElementById('iframe_cotizacion');

// mostrar iframe sistema emision
const boton_emision = document.getElementById('boton_emision');
const iframe_emision = document.getElementById('iframe_emision');

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

const toastDuration = 4000;

let activeToasts = 0;

// Configurar y controlar toasts
if (toastTrigger1) {
  const toastBootstrap1 = bootstrap.Toast.getOrCreateInstance(toastLiveExample1, { delay: toastDuration });
  toastTrigger1.addEventListener('click', () => {
    toastBootstrap1.show();

    columna.classList.add("columna-js");

    toastLiveExample1.addEventListener('hidden.bs.toast', () => {
      columna.classList.remove("columna-js");
    });
  });
}

if (toastTrigger2) {
  const toastBootstrap2 = bootstrap.Toast.getOrCreateInstance(toastLiveExample2, { delay: toastDuration });
  toastTrigger2.addEventListener('click', () => {
    toastBootstrap2.show();

    columna5.classList.add("columna-js5");

    toastLiveExample2.addEventListener('hidden.bs.toast', () => {
      columna5.classList.remove("columna-js5");
    });
  });
}

if (toastTrigger3) {
  const toastBootstrap3 = bootstrap.Toast.getOrCreateInstance(toastLiveExample3, { delay: toastDuration });
  toastTrigger3.addEventListener('click', () => {
    toastBootstrap3.show();

    columna6.classList.add("columna-js6");

    toastLiveExample3.addEventListener('hidden.bs.toast', () => {
      columna6.classList.remove("columna-js6");
    });

  });
}


if (toastTrigger4) {
  const toastBootstrap4 = bootstrap.Toast.getOrCreateInstance(toastLiveExample4, { delay: toastDuration });

  toastTrigger4.addEventListener('click', () => {
    toastBootstrap4.show();
  });
}

if (toastTrigger5) {
  const toastBootstrap5 = bootstrap.Toast.getOrCreateInstance(toastLiveExample5, { delay: toastDuration });

  toastTrigger5.addEventListener('click', () => {
    toastBootstrap5.show();
  });
}

if (toastTrigger6) {
  const toastBootstrap6 = bootstrap.Toast.getOrCreateInstance(toastLiveExample6, { delay: toastDuration });

  toastTrigger6.addEventListener('click', () => {
    toastBootstrap6.show();
  });
}

  // iframes para visualizar el contenido de las plataformas
  boton_emision.addEventListener('click', () => {
  iframe_emision.classList.add('visualizar-iframe1')
});