FROM nfcore/ampliseq:1.2.0

COPY environment.yml /

SHELL ["/bin/bash", "--login", "-c"]

RUN conda env create -f /environment.yml && conda clean -a

COPY bin /opt/conda/envs/ampliseq-test/bin

RUN conda activate ampliseq-test

ENV PATH /opt/conda/envs/ampliseq-test/bin:$PATH