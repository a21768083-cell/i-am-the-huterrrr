
import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Mini Battle Arena",
    page_icon="⚔️",
    layout="wide"
)

# 캐릭터 데이터
CHARACTERS = {
    "warrior": {
        "name": "아르칸",
        "job": "전사 · WARRIOR",
        "weapon": "대검",
        "weapon_desc": "거대한 대검으로 강력한 근접 공격을 가한다.",
        "attack": "회전 베기",
        "attack_desc": "전방의 적을 강하게 베어 피해를 준다.",
        "skill": "블레이드 스톰",
        "skill_desc": "몸을 회전시키며 주변 적에게 연속 피해를 준다.",
        "damage": 95,
        "defense": 90,
        "speed": 55,
        "cooldown": 8,
        "color": "#d97735",
        "emoji": "⚔️",
        "art": "⚔️",
        "story": "왕국을 지키던 전설의 기사. 강력한 검술과 높은 방어력을 자랑한다."
    },
    "mage": {
        "name": "엘리시아",
        "job": "마법사 · MAGE",
        "weapon": "아케인 스태프",
        "weapon_desc": "마력을 증폭시켜 강력한 마법을 사용한다.",
        "attack": "아케인 볼트",
        "attack_desc": "마력 구체를 발사하여 적을 공격한다.",
        "skill": "메테오 스트라이크",
        "skill_desc": "하늘에서 거대한 운석을 떨어뜨려 범위 피해를 준다.",
        "damage": 100,
        "defense": 45,
        "speed": 65,
        "cooldown": 12,
        "color": "#925de8",
        "emoji": "🔮",
        "art": "✨",
        "story": "고대 마법을 계승한 마법사. 압도적인 원거리 공격력을 지녔다."
    },
    "archer": {
        "name": "레이라",
        "job": "궁수 · ARCHER",
        "weapon": "엘븐 롱보우",
        "weapon_desc": "정확하고 빠른 화살 공격에 특화된 장궁.",
        "attack": "정밀 사격",
        "attack_desc": "적을 향해 빠르게 화살을 발사한다.",
        "skill": "레인 오브 애로우",
        "skill_desc": "하늘에서 여러 발의 화살을 쏟아붓는다.",
        "damage": 80,
        "defense": 55,
        "speed": 100,
        "cooldown": 9,
        "color": "#35ad80",
        "emoji": "🏹",
        "art": "🌿",
        "story": "숲의 수호자. 빠른 이동과 정밀한 사격으로 적을 제압한다."
    }
}

# 캐릭터 일러스트 SVG
def make_art(character):
    color = character["color"]

    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg"
         width="400" height="430" viewBox="0 0 400 430">
      <defs>
        <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="{color}" stop-opacity=".65"/>
          <stop offset="100%" stop-color="#111827"/>
        </linearGradient>
        <radialGradient id="glow">
          <stop offset="0%" stop-color="{color}" stop-opacity=".6"/>
          <stop offset="100%" stop-color="{color}" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <rect width="400" height="430" rx="24" fill="url(#bg)"/>
      <circle cx="200" cy="190" r="150" fill="url(#glow)"/>
      <circle cx="200" cy="115" r="48" fill="#f0c9a6"/>
      <path d="M153 112 Q145 35 205 48 Q265 35 248 115
               Q220 80 153 112" fill="#302b38"/>
      <path d="M165 165 L235 165 L270 330
               L130 330 Z" fill="{color}" stroke="#fff"
               stroke-opacity=".4" stroke-width="3"/>
      <path d="M165 175 L110 290 L140 305 L190 215"
            fill="#f0c9a6"/>
      <path d="M235 175 L290 290 L260 305 L210 215"
            fill="#f0c9a6"/>
      <path d="M140 330 L120 400 L190 400 L200 330"
            fill="#252a3c"/>
      <path d="M200 330 L210 400 L280 400 L260 330"
            fill="#252a3c"/>
      <path d="M175 110 L188 110 M212 110 L225 110"
            stroke="#29212a" stroke-width="5" stroke-linecap="round"/>
      <text x="200" y="365" font-size="48"
            text-anchor="middle">{character["art"]}</text>
      <text x="200" y="420" fill="white" font-size="17"
            text-anchor="middle" font-weight="bold">
        {character["job"]}
      </text>
    </svg>
    """
    return "data:image/svg+xml," + urllib.parse.quote(svg)

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(140deg,#0b1020,#17182c,#0b1020);
    color: white;
}
h1,h2,h3 { color: #f5d58c !important; }
.character-card {
    background: linear-gradient(145deg,#25283d,#111525);
    border: 1px solid #46445a;
    border-radius: 15px;
    padding: 12px;
    text-align: center;
    margin-bottom: 12px;
}
.stat-box {
    background: #20243a;
    padding: 13px;
    border-radius: 10px;
    text-align: center;
    border: 1px solid #42435a;
}
.skill-box {
    background: #25283e;
    padding: 18px;
    border-radius: 12px;
    border-left: 4px solid #d6a64c;
    margin: 10px 0;
}
.weapon-box {
    background: #20243a;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #686080;
}
.small-text {color:#b7bfd0;font-size:14px;}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown("""
<div style="text-align:center;padding:20px">
    <h1 style="font-size:42px">⚔ MINI BATTLE ARENA ⚔</h1>
    <p style="color:#b6b8cb;letter-spacing:4px">
        CHOOSE YOUR HERO
    </p>
</div>
""", unsafe_allow_html=True)

if "selected_character" not in st.session_state:
    st.session_state.selected_character = "warrior"

# 캐릭터 선택
st.markdown("## 🏆 캐릭터 선택")

cols = st.columns(3)

for i, (key, char) in enumerate(CHARACTERS.items()):
    with cols[i]:
        selected = st.session_state.selected_character == key

        st.markdown(
            f"""
            <div class="character-card"
                 style="border:2px solid
                 {'#e8bd66' if selected else '#46445a'}">
                <img src="{make_art(char)}"
                     style="width:100%;border-radius:10px">
                <h3>{char['name']}</h3>
                <p style="color:{char['color']}">{char['job']}</p>
                <p class="small-text">{char['weapon']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"{'✓ 선택됨' if selected else '캐릭터 선택'}",
            key=f"select_{key}",
            use_container_width=True
        ):
            st.session_state.selected_character = key
            st.rerun()

# 선택 캐릭터 상세 정보
char = CHARACTERS[st.session_state.selected_character]

st.divider()
st.markdown("## 📜 캐릭터 상세 정보")

left, right = st.columns([1, 1.5])

with left:
    st.image(make_art(char), use_container_width=True)

with right:
    st.markdown(f"# {char['name']}")
    st.markdown(f"### {char['job']}")
    st.write(char["story"])

    st.markdown("### 📊 캐릭터 능력치")

    stats = [
        ("공격력", char["damage"]),
        ("방어력", char["defense"]),
        ("이동속도", char["speed"])
    ]

    for name, value in stats:
        st.markdown(f"**{name} : {value}/100**")
        st.progress(value / 100)

    st.markdown("### ⚔️ 전용 무기")

    st.markdown(
        f"""
        <div class="weapon-box">
            <h3>{char['emoji']} {char['weapon']}</h3>
            <p>{char['weapon_desc']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🗡️ 일반 공격")
    st.markdown(f"**{char['attack']}**")
    st.write(char["attack_desc"])

    st.markdown("### ✨ 전용 스킬")

    st.markdown(
        f"""
        <div class="skill-box">
            <h3>✨ {char['skill']}</h3>
            <p>{char['skill_desc']}</p>
            <p>⏱ 재사용 대기시간: {char['cooldown']}초</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# 게임 시작
st.markdown("## 🎮 전투 준비")

if st.button(
    f"⚔ {char['name']} 선택하고 전투 시작!",
    type="primary",
    use_container_width=True
):
    st.session_state.game_started = True

if st.session_state.get("game_started", False):
    st.success(f"전투 준비 완료! 선택 캐릭터: {char['name']}")
    st.info("다음 단계에서 실제 전투 화면을 연결할 수 있습니다.")
