"""Muscle Therapy Consultant Agent.

A keyword-based consultant that answers questions about muscle therapy,
rehabilitation exercises, stretching, and recovery techniques.
"""


KNOWLEDGE_BASE = {
    "warm_up": {
        "keywords": ["warm up", "warmup", "warm-up", "before exercise", "preparation"],
        "response": (
            "Warm-Up Recommendations:\n"
            "• Spend 5–10 minutes on light aerobic activity (walking, cycling).\n"
            "• Dynamic stretches: leg swings, arm circles, hip rotations.\n"
            "• Gradually increase intensity to raise muscle temperature.\n"
            "• Never skip warm-up — cold muscles are more prone to injury."
        ),
    },
    "cool_down": {
        "keywords": ["cool down", "cooldown", "cool-down", "after exercise", "post workout"],
        "response": (
            "Cool-Down Recommendations:\n"
            "• Spend 5–10 minutes on light activity to lower heart rate gradually.\n"
            "• Static stretches held for 20–30 seconds per muscle group.\n"
            "• Focus on the muscles worked during your session.\n"
            "• Hydrate well and consider foam rolling to aid recovery."
        ),
    },
    "soreness": {
        "keywords": ["sore", "soreness", "doms", "delayed onset", "muscle pain after", "stiff"],
        "response": (
            "Managing Muscle Soreness (DOMS):\n"
            "• Rest: Allow 48 hours before training the same muscle group again.\n"
            "• Ice / Heat: Ice within the first 24 h to reduce inflammation; heat thereafter.\n"
            "• Gentle movement: Light activity and stretching improve blood flow.\n"
            "• Massage or foam rolling can reduce perceived soreness.\n"
            "• Stay hydrated and maintain adequate protein intake for repair."
        ),
    },
    "stretching": {
        "keywords": ["stretch", "stretching", "flexibility", "range of motion", "tight"],
        "response": (
            "Stretching Guidelines:\n"
            "• Static stretching: Hold 20–30 seconds; best after exercise, not before.\n"
            "• Dynamic stretching: Controlled movements through full range; ideal before activity.\n"
            "• PNF stretching: Contract then relax the muscle for deeper flexibility gains.\n"
            "• Stretch to the point of mild tension — never pain.\n"
            "• Consistency matters: daily stretching yields the best long-term results."
        ),
    },
    "massage": {
        "keywords": ["massage", "foam roll", "foam roller", "myofascial", "trigger point", "knot"],
        "response": (
            "Massage & Myofascial Release:\n"
            "• Foam rolling (self-myofascial release) breaks up adhesions and improves circulation.\n"
            "• Spend 30–90 seconds on tender spots, breathing deeply.\n"
            "• Professional sports massage can target deeper trigger points.\n"
            "• Massage 24–48 hours after intense training helps reduce DOMS.\n"
            "• Avoid rolling directly over joints or acutely inflamed areas."
        ),
    },
    "back": {
        "keywords": ["back", "lower back", "lumbar", "spine", "spinal"],
        "response": (
            "Back Muscle Therapy:\n"
            "• Strengthen core muscles (planks, bird-dogs) to support the spine.\n"
            "• Cat-Cow and Child's Pose stretches relieve lumbar tension.\n"
            "• Avoid prolonged sitting — take movement breaks every 30–60 minutes.\n"
            "• Use heat therapy for chronic lower back tightness.\n"
            "• Consult a physiotherapist if pain is sharp, radiating, or persists > 2 weeks."
        ),
    },
    "shoulder": {
        "keywords": ["shoulder", "rotator cuff", "deltoid", "scapula", "trap"],
        "response": (
            "Shoulder Muscle Therapy:\n"
            "• Rotator cuff exercises (external rotation, Y/T/W raises) stabilise the joint.\n"
            "• Doorway stretches improve chest and anterior shoulder flexibility.\n"
            "• Avoid overhead pressing with pain — seek assessment first.\n"
            "• Ice for 15–20 min after activity if the shoulder is inflamed.\n"
            "• Scapular retraction exercises help correct forward-shoulder posture."
        ),
    },
    "leg": {
        "keywords": ["leg", "quad", "hamstring", "calf", "glute", "hip", "knee"],
        "response": (
            "Leg Muscle Therapy:\n"
            "• Quad stretch: Standing or prone, pull heel to glute, hold 30 s each side.\n"
            "• Hamstring stretch: Seated forward fold or supine leg raise.\n"
            "• Calf raises and eccentric lowering strengthen the Achilles complex.\n"
            "• Hip flexor lunge stretches counteract long periods of sitting.\n"
            "• RICE protocol (Rest, Ice, Compression, Elevation) for acute leg strains."
        ),
    },
    "recovery": {
        "keywords": ["recover", "recovery", "rest", "sleep", "nutrition", "hydration"],
        "response": (
            "Muscle Recovery Best Practices:\n"
            "• Sleep 7–9 hours per night — the majority of muscle repair occurs during deep sleep.\n"
            "• Protein intake: 1.6–2.2 g per kg of body weight daily supports muscle synthesis.\n"
            "• Rehydrate: Drink at least 500 ml of water within 30 minutes post-exercise.\n"
            "• Active recovery (light walk, yoga, swimming) on rest days enhances circulation.\n"
            "• Cold-water immersion or contrast showers may accelerate recovery."
        ),
    },
    "injury": {
        "keywords": ["injury", "injured", "strain", "sprain", "tear", "rupture", "pain"],
        "response": (
            "Muscle Injury Guidance:\n"
            "• Acute phase (0–72 hours): POLICE protocol — Protect, Optimal Loading, Ice, Compression, Elevation.\n"
            "• Avoid heat, alcohol, and vigorous activity in the first 48 hours.\n"
            "• Grade I strains usually resolve in 1–3 weeks with conservative care.\n"
            "• Grade II/III strains or suspected tears require professional evaluation.\n"
            "• Return to activity gradually — premature loading risks re-injury.\n"
            "⚠ If pain is severe or does not improve within a week, consult a healthcare professional."
        ),
    },
    "cramp": {
        "keywords": ["cramp", "cramping", "spasm", "charlie horse"],
        "response": (
            "Managing Muscle Cramps:\n"
            "• Gently stretch and massage the affected muscle immediately.\n"
            "• Apply heat to relax the muscle or ice to reduce inflammation.\n"
            "• Hydrate and replenish electrolytes (sodium, potassium, magnesium).\n"
            "• Frequent cramps may indicate dehydration, overtraining, or nutritional deficiencies.\n"
            "• Gradually increasing training load reduces cramp frequency over time."
        ),
    },
}

DEFAULT_RESPONSE = (
    "I'm your Muscle Therapy Consultant. I can help with topics such as:\n"
    "  • Warm-up & cool-down routines\n"
    "  • Muscle soreness & DOMS management\n"
    "  • Stretching & flexibility\n"
    "  • Massage & foam rolling\n"
    "  • Back, shoulder, and leg therapy\n"
    "  • Recovery, nutrition & sleep\n"
    "  • Injury first aid & rehabilitation\n"
    "  • Cramps & muscle spasms\n\n"
    "Please describe your concern or ask a question to get started."
)

GREETING_KEYWORDS = {"hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"}


class MuscleTherapyAgent:
    """Rule-based consultant agent for muscle therapy advice."""

    def consult(self, user_input: str) -> str:
        """Return therapy advice based on *user_input*.

        Parameters
        ----------
        user_input:
            Free-text question or symptom description from the user.

        Returns
        -------
        str
            Formatted advice string.
        """
        if not user_input or not user_input.strip():
            return DEFAULT_RESPONSE

        text = user_input.lower()

        # Greetings
        if any(greet in text for greet in GREETING_KEYWORDS):
            return (
                "Hello! I'm your Muscle Therapy Consultant. 💪\n"
                "How can I help you today? You can ask me about stretching,\n"
                "recovery, injuries, soreness, massage, and more."
            )

        # Match against knowledge base
        matched = []
        for topic, data in KNOWLEDGE_BASE.items():
            if any(kw in text for kw in data["keywords"]):
                matched.append(data["response"])

        if matched:
            return "\n\n".join(matched)

        # Fallback
        return (
            "I'm not sure I understood your question. "
            "Could you rephrase it?\n\n" + DEFAULT_RESPONSE
        )
