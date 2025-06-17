
import os

video_save_path = "inputs\\video\\Apollo.mp4"
# # Change to the EMA-VFI directory and run the interpolation
ema_vfi_dir = r'C:\Users\Shaz Shoaib\Desktop\proj frame gen\EMA-VFI-main\EMA-VFI-main'
interpolate_script = os.path.join(ema_vfi_dir, 'interpolate2.py')
interpolated_output = video_save_path.replace('.mp4', '_interpolated.mp4')


if os.path.exists(interpolate_script):
    # Change working directory and run the command in one shell
    os.system(f'.venv\\Scripts\\activate && python inference_realesrgan_video.py -i"{video_save_path}" -o "{interpolated_output}" -n RealESRGAN_x2plus')
else:
    print(f"Error: Could not find inference_realesrgan_video.py at {interpolate_script}")




video_save_path = "results/Apollo_out.mp4"


# # Change to the EMA-VFI directory and run the interpolation
ema_vfi_dir = r'C:\Users\Shaz Shoaib\Desktop\proj frame gen\EMA-VFI-main\EMA-VFI-main'
interpolate_script = os.path.join(ema_vfi_dir, 'interpolate2.py')
interpolated_output = video_save_path.replace('.mp4', '_interpolated.mp4')

video_path = f"C:\\Users\\Shaz Shoaib\\Desktop\\Real-ESRGAN-master\\Real-ESRGAN-master\\{video_save_path}"
output_path = f"C:\\Users\\Shaz Shoaib\\Desktop\\Real-ESRGAN-master\\Real-ESRGAN-master\\{interpolated_output}"

if os.path.exists(interpolate_script):
    # Change working directory and run the command in one shell
    os.chdir(ema_vfi_dir)
    os.system(f'.venv\\Scripts\\activate && python interpolate2.py "{video_path}" --output "{output_path}"')
else:
    print(f"Error: Could not find interpolate2.py at {interpolate_script}")
