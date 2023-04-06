cd /
source "${HOME}/conda/etc/profile.d/conda.sh"
source "${HOME}/conda/etc/profile.d/mamba.sh"
conda activate

gunicorn -w 10 -b 0.0.0.0:80 'code:app'