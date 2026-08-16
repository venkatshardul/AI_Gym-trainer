import streamlit as st
from service.auth.login_wall import render_login_wall
from service.state.session_default import initial_session_defaults
from service.config.workout_config import EXERCISES_OPTIONS
import os
from service.ui.style_loader import load_css,inject_local_css_content,inject_local_font



def main():
    
    st.set_page_config(
        page_icon="💪",
        page_title="GymSync",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    load_css(os.path.join(os.getcwd(), "static","css","style.css"))
    
    

    if not render_login_wall(): 
        return

    initial_session_defaults()

    workout_started = st.session_state.get("workout_started", False)


    # Sidebar
    with st.sidebar:
        st.title("GymSync")
        

        if st.session_state.username:
            st.caption(f"Login as: {st.session_state.username}")
            
        else:
            st.caption("Not logged in")
        
        
        st.divider()

        st.subheader("Workouts")

        if not workout_started:
            exercise = st.selectbox("Choose your exercise",options=EXERCISES_OPTIONS,key="plan_exercise")
            
            st.number_input("Number of sets",min_value=1,max_value=10,value=3,key="plan_sets",step=1)

            st.number_input("Number of reps",min_value=1,max_value=20,value=10,key="plan_reps",step=1)
            
            if st.button("Start Workout",key="start_workout",width="stretch"):

                st.session_state.workout_started = True
                st.rerun()
        else:
            exercise=st.session_state.get("plan_exercise")
            sets=st.session_state.get("plan_sets")
            reps=st.session_state.get("plan_reps")

            print(f"{exercise} , {sets} , {reps}")

            st.info(f"Current Exercise: {exercise} — {sets}/{reps}")

            end_session_button = st.button("End Session",key="end_session",width="stretch")

            if end_session_button:
            
                st.session_state.workout_started = False
                st.rerun()

        if workout_started:
            st.divider()

            exercise=st.session_state.get("plan_exercise")
            
            total_reps = st.session_state.get("reps") * st.session_state.get("plan_reps")
            current_set_reps=st.session_state.get("current_set_reps")
            reps_per_set=st.session_state.get("plan_reps")
            target_sets=st.session_state.get("plan_sets")
            sets_completed=st.session_state.get("sets_completed")
            
            
            st.subheader("Current workout")

            st.metric("Total Reps",total_reps)
            st.metric("Current Set",f"{current_set_reps}/{reps_per_set}")
            st.metric("Sets Completed",f"{sets_completed}/{target_sets}")
            
            
            st.divider()

            if exercise == "Squats":
                st.subheader("Squats Metrics")
                st.metric("Knee Angle",st.session_state.get("knee_angle"))
                st.metric("Back Angle",st.session_state.get("back_angle"))
                st.metric("Elbow Angle",st.session_state.get("elbow_angle"))
                st.metric("Front Knee Angle",st.session_state.get("front_knee_angle"))
                st.metric("Torso Angle",st.session_state.get("torso_angle"))
           
            elif exercise == "Push-ups":
                st.subheader("Push-ups Metrics")
                st.metric("Knee Angle",st.session_state.get("knee_angle"))
                st.metric("Back Angle",st.session_state.get("back_angle"))
                st.metric("Elbow Angle",st.session_state.get("elbow_angle"))
                st.metric("Front Knee Angle",st.session_state.get("front_knee_angle"))
                st.metric("Torso Angle",st.session_state.get("torso_angle"))
            
            elif exercise == "Lunges":
                st.subheader("Lunges Metrics")
                st.metric("Knee Angle",st.session_state.get("knee_angle"))
                st.metric("Back Angle",st.session_state.get("back_angle"))
                st.metric("Elbow Angle",st.session_state.get("elbow_angle"))
                st.metric("Front Knee Angle",st.session_state.get("front_knee_angle"))
                st.metric("Torso Angle",st.session_state.get("torso_angle"))
            
            
            elif exercise == "Biceps Curls (Dmbbell)":
                st.subheader("Biceps Curls (Dmbbell) Metrics")
                st.metric("Knee Angle",st.session_state.get("knee_angle"))
                st.metric("Back Angle",st.session_state.get("back_angle"))
                st.metric("Elbow Angle",st.session_state.get("elbow_angle"))
                st.metric("Front Knee Angle",st.session_state.get("front_knee_angle"))
                st.metric("Torso Angle",st.session_state.get("torso_angle"))
            
            
            elif exercise == "Shoulder Press":
                st.subheader("Shoulder Press Metrics")
                st.metric("Knee Angle",st.session_state.get("knee_angle"))
                st.metric("Back Angle",st.session_state.get("back_angle"))
                st.metric("Elbow Angle",st.session_state.get("elbow_angle"))
                st.metric("Front Knee Angle",st.session_state.get("front_knee_angle"))
                st.metric("Torso Angle",st.session_state.get("torso_angle"))
            
            
            elif exercise == "Crunches":
                st.subheader("Crunches Metrics")
                st.metric("Knee Angle",st.session_state.get("knee_angle"))
                st.metric("Back Angle",st.session_state.get("back_angle"))
                st.metric("Elbow Angle",st.session_state.get("elbow_angle"))
                st.metric("Front Knee Angle",st.session_state.get("front_knee_angle"))
                st.metric("Torso Angle",st.session_state.get("torso_angle"))

          
        


     
    st.write(f"welcome to the app {st.session_state.username}")

if __name__ == "__main__":
    main()