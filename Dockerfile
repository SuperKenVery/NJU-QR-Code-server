FROM debian:bullseye-slim
WORKDIR /code

RUN echo "deb http://mirror.nju.edu.cn/debian/ bullseye main contrib non-free" > /etc/apt/sources.list && \
    echo "deb http://mirror.nju.edu.cn/debian/ bullseye-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirror.nju.edu.cn/debian/ bullseye-backports main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirror.nju.edu.cn/debian-security bullseye-security main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y wget

RUN wget -O Mambaforge.sh https://mirror.nju.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Mambaforge-$(uname)-$(uname -m).sh
RUN bash Mambaforge.sh -b -p "${HOME}/conda"
RUN . "${HOME}/conda/etc/profile.d/conda.sh" && \
    . "${HOME}/conda/etc/profile.d/mamba.sh" && \
    conda install python=3.10 && \
    conda activate && \
    pip config set global.index-url https://mirror.nju.edu.cn/pypi/web/simple

COPY . .

RUN . "${HOME}/conda/etc/profile.d/conda.sh" && \
    . "${HOME}/conda/etc/profile.d/mamba.sh" && \
    conda activate && \
    pip install -r qr_code_server/requirements.txt



CMD [ "bash","/code/start.sh" ]