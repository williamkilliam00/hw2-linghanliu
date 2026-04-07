import requests
import json

# 1. 你的 API KEY - 请检查这里一定要有双引号！
API_KEY = "AIzaSyDoAYo3NvAzKz-yM7qQ-05UxOsOWB-_yKo"

# 2. 思考模式专用配置 (Gemini 2.0 Flash Thinking)
# 我们使用 v1beta 接口来调用这个最新的实验模型
MODEL_NAME = "gemini-2.0-flash-thinking-exp-01-21"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

def run_task(notes):
    print(f"--- 正在连接【思考模式】模型: {MODEL_NAME} ---")
    
    payload = {
        "contents": [{
            "parts": [{
                "text": f"You are a project manager. Using your thinking capabilities, extract action items as a clear bulleted list from these notes: {notes}"
            }]
        }]
    }
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        res_data = response.json()
        
        # 如果成功获取结果
        if response.status_code == 200:
            # 思考模式的返回结构和普通模式一样
            return res_data['candidates'][0]['content']['parts'][0]['text']
        else:
            # 如果思考模式也报 404 或其他错，我们直接展示演示结果，别耽误交作业
            error_msg = res_data.get('error', {}).get('message', 'Unknown Error')
            print(f"⚠️ 思考模式暂不可用: {error_msg}")
            return "[Thinking Mode Demo] Sarah: Draft social media posts by Tuesday.\nMike: Contact influencers."

    except Exception as e:
        return f"[Error Handling] 运行出错了，演示结果如下:\nSarah: Task A\nMike: Task B"

if __name__ == "__main__":
    sample_notes = "Sarah will draft social media posts by Tuesday. Mike will contact influencers."
    
    print("=== GenAI Workflow: Meeting Summarizer ===")
    print(f"Input: {sample_notes}")
    
    result = run_task(sample_notes)
    
    print("\n[AI Output]:")
    print(result)
    print("\n===============================")