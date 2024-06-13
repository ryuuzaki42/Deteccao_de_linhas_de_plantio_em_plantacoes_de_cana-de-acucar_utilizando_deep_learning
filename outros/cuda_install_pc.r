
https://www.tensorflow.org/install/gpu
https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-windows

1 Drivers de GPU NVIDIA®: a CUDA® 11.2 exige 450.80.02 ou mais recente.

2 CUDA® Toolkit: o TensorFlow suporta a CUDA® 11.2 (TensorFlow >= 2.5.0).

3 cuDNN SDK 8.1.0 versões da cuDNN.
    3.1 zlib

## cuda
    https://developer.nvidia.com/cuda-toolkit-archive
        > CUDA Toolkit 11.5.0 (October 2021), Versioned Online Documentation

            > Windows
            > x86_64
            > 10
            > exe (local)

            2.4 GB

        https://developer.nvidia.com/cuda-11-5-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local

            cuda_11.5.0_496.13_win10.exe

    ## Install - take a long time

## cudnn
    # https://developer.nvidia.com/rdp/cudnn-download

    https://developer.nvidia.com/rdp/cudnn-archive
        > Download cuDNN v8.3.2 (January 10th, 2022), for CUDA 11.5

    ## Need cudnn account or nvidia account

    ## Extract
    ## Copy all in "cudnn-windows-x86_64-8.3.2.44_cuda11.5-archive\bin"
    ## to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\bin"

## Error
    # https://stackoverflow.com/questions/69879188/could-not-load-library-cudnn-cnn-infer64-8-dll-error-code-126
    "Could not load library cudnn_cnn_infer64_8.dll. Error code 126
    Please make sure cudnn_cnn_infer64_8.dll is in your library path!"

    ## "Install zlib"
        https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-zlib-windows

    ## Download
        http://www.winimage.com/zLibDll/zlib123dllx64.zip

    ## Extract
    ## Copy "zlibwapi.dll" in "zlib123dllx64\dll_x64"
    ## to "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\bin"

    ## PATH
        ## Print PATH
            echo %PATH:;=&echo.%

            ...
            C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\bin
            C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\libnvvp
            ...

# test if need
    SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\bin;%PATH%
    SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\extras\CUPTI\lib64;%PATH%
    SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\include;%PATH%
    SET PATH=C:\tools\cuda\bin;%PATH%
