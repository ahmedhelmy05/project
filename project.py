import tkinter as tk
from tkinter import messagebox
import yt_dlp
import webbrowser


def get_video_url(resolution):
    url = url_entry.get()
    if not url:
        messagebox.showerror("خطأ", "الرجاء إدخال رابط الفيديو")
        return
    
    # دالة للتنسيق المناسب
    def extract_url(ydl_opts):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                return info_dict['url']
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء استخراج الرابط: {e}")
            return None

   
    if resolution == "high":
        ydl_opts = {'format': 'best'}
    elif resolution == "low":
        ydl_opts = {'format': 'worst'}
    elif resolution == "audio":
        ydl_opts = {'format': 'bestaudio'}
    else:
        messagebox.showerror("خطأ", "خيار غير صالح")
        return

  
    video_url = extract_url(ydl_opts)
    if video_url:
        webbrowser.open(video_url)  
    else:
        messagebox.showerror("خطأ", "تعذر العثور على الرابط")


root = tk.Tk()
root.title("عرض فيديو من اليوتيوب")
root.geometry("400x200")


tk.Label(root, text="ضع رابط الفيديو هنا:", font=("Arial", 12)).pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)


tk.Button(root, text="عرض بجودة عالية", command=lambda: get_video_url("high"), width=20).pack(pady=5)
tk.Button(root, text="عرض بجودة منخفضة", command=lambda: get_video_url("low"), width=20).pack(pady=5)
tk.Button(root, text="عرض الصوت فقط", command=lambda: get_video_url("audio"), width=20).pack(pady=5)

root.mainloop()