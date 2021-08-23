# Example demonstration of container networking with the FLASK REST framework

This project should serve for demonstration purposes and testing.

# Installation

Installation requires Docker.

Relevant cmds for starting single container:
`docker build -t flask-bioinformatics:1.0 -f bioinformatics.dockerfile .`,
`docker run -d -t -p 5001:5001 -v ${PWD}:/application --name flask-mafft-fasttree flask-bioinformatics:1.0`

Installation of this example application can be performed with `docker-compose up`.
