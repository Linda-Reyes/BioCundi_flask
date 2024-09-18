// Sitio Oficial de Chart.js
// https://www.chartjs.org/docs/latest/samples/information.html
let chartjs1;
let chartjs2;

function mostrarTorta(){
    const contendor2 = document.getElementById('chart-pie-container');
    const canvas2 = document.getElementById('canvas2');
    const titulo2 = document.getElementById('titulo2');
    const tipoTorta = document.getElementById('tipoTorta').value;
    const ctx = canvas2.getContext('2d');    

    contendor2.style.display = 'block';
    if( chartjs2 ) chartjs2.destroy();    
    fetch('/data')
        .then(response => response.json() )
        .then(data => {
            titulo2.innerHTML = data.titulo;
            chartjs2 = new Chart(ctx, {
                type: tipoTorta,
                data: {
                    labels: data.especies,
                    datasets: [{
                        label: data.titulo,
                        data: data.observaciones,
                        backgroundColor:  [
                            'rgb(255, 99, 132)',
                            'rgb(255, 159, 64)',
                            'rgb(255, 205, 86)',
                            'rgb(75, 192, 192)',
                            'rgb(54, 162, 235)',
                            'rgb(153, 102, 255)',
                            'rgb(201, 203, 207)'
                          ],
                        hoverOffset: 4,                        
                    }]
                }
            });
        });
}

function mostrarBarra(){
    const contendor1 = document.getElementById('chart-bar-container');
    const canvas1 = document.getElementById('canvas1');
    const titulo1 = document.getElementById('titulo1');
    const tipoBarra = document.getElementById('tipoBarra').value;
    const ctx = canvas1.getContext('2d');    

    contendor1.style.display = 'block';
    if( chartjs1 ) chartjs1.destroy();
    fetch('/data')
        .then(response => response.json() )
        .then(data => {
            titulo1.innerHTML = data.titulo;
            chartjs1 = new Chart(ctx, {
                //type: 'bar', //'bar', 'line'
                type: tipoBarra,
                data: {
                    labels: data.especies,
                    datasets: [{
                        label: '',
                        data: data.observaciones,
                        backgroundColor:  [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 159, 64, 0.2)',
                            'rgba(255, 205, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(201, 203, 207, 0.2)'
                          ],
                          borderColor: [
                            'rgb(255, 99, 132)',
                            'rgb(255, 159, 64)',
                            'rgb(255, 205, 86)',
                            'rgb(75, 192, 192)',
                            'rgb(54, 162, 235)',
                            'rgb(153, 102, 255)',
                            'rgb(201, 203, 207)'
                          ],
                        borderWith: 1,
                        pointStyle: 'rectRounded',
                        pointRadius: 5,
                    }]
                },
                options: {
                    indexAxis: 'y',                    
                    plugins: {
                        title: {
                            display: true,
                            text: data.titulo,
                            color: 'rgb(0,0,0)'
                        }
                    }
                }
            })
        });//fetch
}//mostrarBarra