
    ## Anaconda ##

# Autor= João Batista Ribeiro
# Bugs, Agradecimentos, Críticas "construtivas"
# Mande me um e-mail. Ficarei Grato!
# e-mail: joao42lbatista@gmail.com
#
# Last update: 31/12/2022

## Download
https://www.anaconda.com/
https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh

$ md5sum Anaconda3-2022.10-Linux-x86_64.sh
80256bd7a55509665c4179fd61516745  Anaconda3-2022.10-Linux-x86_64.sh

## Install
./Anaconda3-*-Linux-x86_64.sh

    # Agreements
    > yes

    > Location to install
/media/sda2/home/j/.0installed/anaconda3

    # Activate change .bashrc and other files
    > yes

## Disable conda base environment activated on startup
    # Set the auto_activate_base parameter to false:
conda config --set auto_activate_base false

    # user config file : /media/sda2/home/j/.condarc
        > auto_activate_base: false

## To activate base env
conda activate

    ## info
conda info

    ## deactivate
conda deactivate

## Conda code added in .bashrc
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/media/sda2/home/j/.0installed/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/media/sda2/home/j/.0installed/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/media/sda2/home/j/.0installed/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/media/sda2/home/j/.0installed/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

## To create an environment - myenv is the name
    # --name or -n
conda create --name myenv

    # Package Plan
    environment location: /media/sda2/home/j/.0installed/anaconda3/envs/myenv

    ## To activate this environment
conda activate myenv

    ## To deactivate this environment
conda deactivate

## Create in local folder
    cd /media/sda2/home/j/.0installed/

    # --prefix or -p
conda create --prefix test_env

    # Package Plan
    environment location: /media/sda2/home/j/.0installed/test_env

    ## To activate this environment, use
conda activate /media/sda2/home/j/.0installed/test_env

    ## Create a symbolic link to be more easy to activate
        ln -s /media/sda2/home/j/.0installed/test_env/ /media/sda2/home/j/.0installed/anaconda3/envs/

        conda activate test_env

## list envs
conda env list

conda info --envs

## Delete environment
    ## Be careful
conda env remove --name ENVIRONMENT

conda env remove --name myenv

    ## Or in specify place
conda env remove --prefix /path/to/env

conda env remove --prefix /media/sda2/envs/test_env

## To create an environment with a specific version of Python
conda create -n myenv python=3.6

## To create an environment with a specific package
conda create -n myenv scipy

## To create an environment with a specific version of a package
conda create -n myenv scipy=0.15.0

## Install package
    # https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment/44066694

    ## Install pip
conda install pip

        # This will install pip to your venv directory
        # Find the actual venv folder
        # It should be somewhere like anaconda/envs/venv_name/
            conda env list

    ## Install new packages by doing
        anaconda3/envs/venv_name/bin/pip install package_name

    ## See pip bin/path command
        which -a pip

pip install opencv-python
pip install jupyter
pip install matplotlib
pip install scikit-image
pip install keras
pip install pandas
pip install tensorflow
pip install spyder

pip install segmentation-models
pip install keras-segmentation
pip install sklearn

## nbdime
pip install nbdime

    ## Terminal
        nbdiff notebook_1.ipynb notebook_2.ipynb

    ## web-based
nbdiff-web notebook_1.ipynb notebook_2.ipynb

## jupyter_contrib_nbextensions - inside jupyter-notebook
    # https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html

    !pip install jupyter_contrib_nbextensions
    !jupyter contrib nbextension install --user
    !jupyter nbextension enable varInspector/main

    ## Enable
        L1
            Collapsible Headings
            Highlight selected word

        L2
            ExecuteTime
            Table of Contents
            Variable Inspector

        L3
            contrib_nbextensions_help_item
            Hinterland
            Nbextensions dashboard tab
            Snippets Menu

        L4
            Nbextensions edit menu item
            spellchecker

## list all packages installed
conda list

## pip remove package
pip uninstall tensorfow

## Conda clean Remove unused packages and caches
conda clean --all

## Clean pip cache
    ## location of the cache
pip cache dir

    ## clear all wheel files from pip's cache
pip cache purge

## conda save env package requirements.txt

    ## Activate one env
conda activate deeplearning-py37

    ## CMD move to E:\\
e:

    ## Move to folder Joao
cd Joao

    ## List packages installed
conda list -e

    ## Save list package installed in a file
conda list -e > deeplearning-py37_requirements.txt

conda list -e > test-env_JB_requirements.txt

    ## Create a env with requirements.txt
        # conda create --name <env> --file <this file>
        # conda create --prefix ./<path_env> --file <this file>
conda create --prefix ./test_2_env --file conda_requirements\deeplearning-py37_requirements.txt

conda create --prefix ./test_2_env --file conda_requirements\deeplearning-py37_requirements_no_version.txt

    ## Delete env
conda env remove -n test_2_env

conda env remove --prefix test_2_env/
