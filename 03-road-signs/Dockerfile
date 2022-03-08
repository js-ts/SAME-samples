# new enough python for SAME (3.8), old enough that it still works in kf 1.2
FROM public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-tensorflow:v1.3.0
USER root
RUN apt-get update && apt-get install -y python3-opencv
USER jovyan
RUN pip install opencv-python scikit-image matplotlib
RUN pip install sameproject==0.1.6
RUN pip install dotscience
ENV GRANT_SUDO=yes
