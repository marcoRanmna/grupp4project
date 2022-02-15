var ctx = document.getElementById("lineChart").getContext("2d");
        var lineChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: {{ labels | safe }},
                datasets: [
                    {
                        label: "Data points",
                        data: {{ values | safe }},
                        fill: true,
                        borderColor: "rgb(75, 192, 192)",
                        lineTension: 0.5

                    }
                ]
            },
            options: {
                responsive: false
            }

        });