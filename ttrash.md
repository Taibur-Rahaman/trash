# Department of Electrical and Computer Engineering

**North South University**

---

# Directed Research

**SOFTWARE ENGINEERING INTERNSHIP AT FLYMEK DRONE MANUFACTURING**

---

**Kazi Eraj Al Minhaj Turjo**  ID# 183106642

---

**Faculty Advisor:**

Dr. ASM Jahid Hasan

Assistant Professor

ECE Department

**Fall, 2025**

---

# APPROVAL

Kazi Eraj Al Minhaj Turjo (ID # 183106642) from Electrical and Computer Engineering Department of North South University, has worked on the Internship Project titled "Software Engineering Internship at FlyMek Drone Manufacturing" under the supervision of Dr. ASM Jahid Hasan for partial fulfillment of the requirement for the degree of Bachelors of Science in Engineering and has been accepted as satisfactory.

**Supervisor's Signature**

…………………………………….

Dr. ASM Jahid Hasan

Assistant Professor

Department of Electrical and Computer Engineering

North South University

Dhaka, Bangladesh.

**Chairman's Signature**

…………………………………….

Dr. Rajesh Palit

Professor

Department of Electrical and Computer Engineering

North South University

Dhaka, Bangladesh.

---

# DECLARATION

This is to declare that this project/internship report is my original work. No part of this work has been submitted elsewhere partially or fully for the award of any other degree or diploma. All project related information will remain confidential and shall not be disclosed without the formal consent of the project supervisor. Relevant previous works presented in this report have been properly acknowledged and cited. The plagiarism policy, as stated by the supervisor, has been maintained.

**Student's name & Signature**

1. Kazi Eraj Al Minhaj Turjo

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

---

# ACKNOWLEDGEMENTS

The author would like to express heartfelt gratitude towards the project and research supervisor, Dr. ASM Jahid Hasan, Assistant Professor, Department of Electrical and Computer Engineering, North South University, Bangladesh, for invaluable support, precise guidance and advice pertaining to the internship work, research and theoretical studies carried out during the course of the current internship period and also in the preparation of the current report.

Furthermore, the author would like to thank the Department of Electrical and Computer Engineering, North South University, Bangladesh for facilitating the internship program. The author would also like to express gratitude to the site supervisor and the engineering team at FlyMek Drone Manufacturing for providing the opportunity to work in a professional environment and for guiding during the internship period. Their support and cooperation played an important role in learning and development. The author would also like to thank colleagues and staff members at FlyMek Drone Manufacturing for their valuable cooperation and assistance throughout the internship. The author would also like to thank loved ones for their countless sacrifices and continual support.

---

# ABSTRACT

**Software Engineering Internship at FlyMek Drone Manufacturing**

This report describes the internship experience at FlyMek Drone Manufacturing, where the author worked as a Software Engineering Intern in the Information Technology department. The internship was conducted from 14 September 2025 to 15 December 2025 and focused on internal software systems used for drone testing, control, and data monitoring. The drone industry has grown rapidly due to advancements in sensors, embedded systems, and software technologies, creating a demand for reliable software systems and user-friendly interfaces for UAV operations. During the internship, the author assisted in the development and maintenance of internal software tools, supported the integration of communication protocols such as MAVLink, and contributed to UI/UX improvements for ground control applications including QGroundControl. The work also involved automation scripts, real-time data monitoring systems, and troubleshooting hardware–software interaction issues. The methodology followed a structured work process under the guidance of senior engineers, involving hands-on experience with software systems, protocol integration support, UI/UX enhancement tasks, and real-time data monitoring activities. Key results included improved understanding of telemetry data handling, enhanced user interface clarity in ground control applications, and successful support for automation and data monitoring systems. The internship demonstrated that reliable drone operation depends heavily on well-maintained software systems and proper integration between hardware and software components. This experience provided practical exposure to software engineering concepts, improved professional skills including teamwork and documentation, and strengthened the foundation for future academic and professional opportunities in software engineering.

---

# TABLE OF CONTENTS

LETTER OF TRANSMITTAL ........................................................ ii

APPROVAL ........................................................................... iv

DECLARATION ....................................................................... v

ACKNOWLEDGEMENTS ........................................................... vi

ABSTRACT ............................................................................ vii

TABLE OF CONTENTS ............................................................ viii

LIST OF FIGURES .................................................................. x

LIST OF TABLES .................................................................... xi

**Chapter 1 Introduction** ......................................................... 1

1.1 Background and Motivation ................................................ 1

1.2 Purpose and Goal of the Project ........................................... 1

1.3 Organization of the Report ................................................... 2

**Chapter 2 Research Literature Review** ....................................... 3

2.1 Existing Research and Limitations ........................................ 3

**Chapter 3 Methodology** ......................................................... 4

3.1 System Design ................................................................... 4

3.2 Hardware and/or Software Components ................................. 5

3.3 Hardware and/or Software Implementation ............................ 6

**Chapter 4 Investigation/Experiment, Result, Analysis and Discussion** ... 8

**Chapter 5 Conclusions** ........................................................... 10

5.1 Summary .......................................................................... 10

5.2 Limitations ........................................................................ 10

5.3 Future Improvement ........................................................... 11

**References** .......................................................................... 12

---

# LIST OF FIGURES

[Figures would be listed here with page numbers]

---

# LIST OF TABLES

TABLE I. SOFTWARE AND HARDWARE TOOLS USED DURING INTERNSHIP .......... 5

---

# Chapter 1 Introduction

## 1.1 Background and Motivation

Unmanned Aerial Vehicles (UAVs), commonly known as drones, are increasingly being used in various applications such as surveying, inspection, monitoring, and data collection. Behind the operation of these systems lies a combination of hardware components and software platforms that ensure stable communication, control, and data processing [1]. The drone industry has grown rapidly due to advancements in sensors, embedded systems, and software technologies. Modern drone operations rely heavily on ground control software, communication protocols, and real-time data processing systems [2].

Software engineering plays a vital role in UAV systems, particularly in areas such as ground control software, telemetry data handling, user interface design, and automation. As drones become more widely used, the demand for reliable software systems and user-friendly interfaces has increased significantly. Software engineers play a crucial role in ensuring that these systems function smoothly and provide accurate information to operators [3].

The motivation for this internship was to gain practical exposure to these software-based aspects of drone systems and to understand how theoretical knowledge acquired through academic coursework is applied in an industrial environment. This internship provided an opportunity to work in a professional setting where real software development workflows could be observed, collaboration with engineers could be experienced, and contributions to ongoing projects related to drone software systems could be made.

## 1.2 Purpose and Goal of the Project

The main purpose of this internship was to gain practical experience in software engineering within a drone technology company. The specific goals and objectives of the internship were:

- To assist in the development and maintenance of internal software systems used for drone testing, monitoring, and control operations
- To support communication protocol integration, particularly MAVLink-based frameworks
- To contribute to UI/UX enhancements for ground control software applications such as QGroundControl
- To understand real-time data monitoring and automation systems used in drone operations
- To improve professional skills including teamwork, problem-solving, and documentation practices
- To bridge the gap between academic learning and professional practice by applying theoretical knowledge in a real industrial environment

The scope of the internship was limited to supporting and assisting ongoing software development activities. The work focused on software tools, interfaces, data handling, and system support tasks rather than flight-critical firmware development.

## 1.3 Organization of the Report

This report is organized into five main chapters. Chapter 1 provides the introduction, including background information about the drone industry and the motivation for undertaking this internship. Chapter 2 presents a literature review of existing research related to drone software systems, communication protocols, and ground control software. Chapter 3 describes the methodology followed during the internship, including system design, hardware and software components used, and implementation details. Chapter 4 presents the investigation, experiments, results, analysis, and discussion of the work performed during the internship period. Finally, Chapter 5 provides conclusions, including a summary of the work, limitations encountered, and suggestions for future improvements.

---

# Chapter 2 Research Literature Review

## 2.1 Existing Research and Limitations

Research in drone software systems has focused on various aspects including ground control software, communication protocols, telemetry data handling, and user interface design. MAVLink (Micro Air Vehicle Link) is a widely used communication protocol for drones that enables communication between ground control stations and unmanned vehicles [4]. The protocol supports various message types for telemetry data, command and control, and parameter configuration. Research has shown that proper implementation of MAVLink is crucial for reliable drone operations [5].

Ground control software such as QGroundControl has been extensively used in the drone industry for mission planning, real-time monitoring, and vehicle control [6]. Studies have emphasized the importance of user-friendly interfaces in ground control applications to reduce operator workload and improve mission success rates [7]. Research has also highlighted the significance of real-time data processing and visualization in drone operations [8].

Recent studies have focused on improving the reliability and efficiency of drone software systems. Research has shown that proper data logging and monitoring systems are essential for performance evaluation and troubleshooting [9]. Automation scripts and data processing tools have been developed to streamline drone testing and monitoring processes [10].

However, several limitations have been identified in existing research and industry practices. Many studies focus on individual components of drone software systems without addressing the integration challenges between different software modules. There is limited research on the practical implementation challenges faced in industrial settings, particularly regarding legacy systems and compatibility issues. Additionally, most research focuses on flight-critical systems, with less attention given to internal testing and monitoring tools used during development phases.

The following observations have been made after a detailed examination of the literature reviews: (i) most articles focus on flight-critical systems rather than internal development and testing tools, (ii) there is limited documentation on practical implementation challenges in industrial environments, (iii) integration between different software components and communication protocols is often not thoroughly addressed, and (iv) user interface improvements for ground control software are often discussed theoretically without detailed implementation guidance. These observations motivated the focus of this internship on practical software engineering tasks including internal tool development, protocol integration support, UI/UX improvements, and real-time data monitoring systems.

---

# Chapter 3 Methodology

## 3.1 System Design

The internship followed a structured work process under the guidance of senior engineers. The overall system design involved working with internal software systems that support drone testing, monitoring, and control operations. The system architecture consisted of several key components:

1. **Ground Control Software**: Applications such as QGroundControl that provide interfaces for mission planning, real-time monitoring, and vehicle control
2. **Communication Protocol Layer**: MAVLink-based frameworks that handle telemetry data transmission between drones and ground stations
3. **Data Processing and Monitoring Systems**: Tools for logging, processing, and visualizing telemetry data in real-time
4. **Automation Scripts**: Scripts for automating testing procedures and data processing tasks
5. **User Interface Components**: Dashboard and control interfaces that display system status and allow operator interaction

The workflow typically involved receiving telemetry data from drones through MAVLink protocols, processing this data in ground control applications, displaying information through user interfaces, and logging data for analysis. The internship work focused on supporting improvements and maintenance of these various components.

A simplified block diagram of the system architecture would show:
- Drone Hardware → MAVLink Communication → Ground Control Software → Data Processing → User Interface/Display
- Automation Scripts → Testing Procedures → Data Logging → Performance Analysis

## 3.2 Hardware and/or Software Components

During the internship, various hardware and software components were utilized. The following table provides details of the main tools and technologies used:

**TABLE I. SOFTWARE AND HARDWARE TOOLS USED DURING INTERNSHIP**

| Tool | Functions | Other similar Tools (if any) | Why selected this tool |
|------|-----------|------------------------------|----------------------|
| QGroundControl | Ground control station software for mission planning, real-time monitoring, and vehicle control | Mission Planner, APM Planner | Industry standard, widely used, open-source |
| MAVLink Protocol | Communication protocol for transmitting telemetry data and commands between drones and ground stations | Custom protocols, ROS | Standard protocol, well-documented, widely supported |
| Internal Software Systems | Custom software tools for drone testing, monitoring, and data processing | Custom solutions | Company-specific requirements |
| Automation Scripts | Python/bash scripts for automating testing and data processing tasks | Various scripting languages | Flexibility, ease of use, integration capabilities |
| Documentation Tools | Tools for recording technical progress and maintaining documentation | Various documentation platforms | Standard practice, knowledge management |

**Software Components:**

- **Ground Control Software**: QGroundControl and related dashboard applications for monitoring and controlling drone operations
- **Communication Frameworks**: MAVLink-based communication systems for telemetry data transmission
- **Development Tools**: Programming environments and tools for software development and debugging
- **Automation Tools**: Scripting languages and automation frameworks for testing and data processing
- **Documentation Systems**: Tools for maintaining technical documentation and progress tracking

**Hardware Components:**

- **Drone Systems**: Various UAV platforms used for testing and development
- **Communication Hardware**: Radio modules and communication devices for MAVLink data transmission
- **Computing Systems**: Workstations and development computers for running ground control software and development tools
- **Testing Equipment**: Hardware components used for system testing and validation

## 3.3 Hardware and/or Software Implementation

The implementation work during the internship involved several key areas:

**Software Tool Maintenance and Improvement:**
The internship involved assisting in maintaining and improving internal software tools by fixing minor issues, supporting feature updates, and testing system behavior. This included debugging code, implementing small feature enhancements, and ensuring compatibility between different software components.

**MAVLink Protocol Integration Support:**
Work was performed to support the integration of MAVLink communication protocols by observing how telemetry data is received, processed, and displayed in ground control applications. This involved understanding message formats, data parsing, and ensuring proper synchronization between different system components. Although core protocol implementations were not modified, support was provided for testing and troubleshooting communication issues.

**UI/UX Improvements:**
Significant effort was dedicated to supporting UI/UX improvements for applications like QGroundControl and related dashboards. This included improving layout clarity, ensuring better data visualization, and testing interface responsiveness. Work involved reorganizing data fields, improving visual prioritization, and ensuring that critical information was easily accessible to operators.

**Automation and Data Monitoring:**
Implementation work included assisting in tasks related to data logging, monitoring system performance, and verifying that real-time data streams were functioning correctly. This involved creating and modifying automation scripts, setting up monitoring systems, and ensuring accurate data capture and storage.

**Testing and Validation:**
Throughout the implementation process, extensive testing was performed to ensure that changes did not introduce new issues and that system behavior met expected requirements. This included functional testing, integration testing, and validation of real-time data processing capabilities.

The implementation followed standard software development practices including version control, code review processes, and documentation maintenance. All work was performed under the supervision of senior engineers to ensure quality and adherence to company standards.

---

# Chapter 4 Investigation/Experiment, Result, Analysis and Discussion

During the internship period, several investigations and experiments were conducted as part of the software engineering work at FlyMek Drone Manufacturing. The following sections describe the key activities, results, and analyses.

**Investigation of Telemetry Data Handling:**
One of the primary investigations involved understanding how telemetry data flows through the system from drone hardware to ground control applications. Through continuous exposure to these systems, observations were made regarding how telemetry data is collected, transmitted via MAVLink protocols, processed by ground control software, and displayed to operators. Analysis revealed that proper data synchronization and consistency are crucial for reliable system operation. Communication delays or inconsistencies were found to significantly affect data reliability and operator decision-making.

**MAVLink Communication Protocol Analysis:**
While assisting in MAVLink-based communication support, analysis was performed on how telemetry messages are received by ground control applications. Observations indicated that message parsing, error handling, and retry mechanisms play important roles in maintaining communication reliability. Although core protocol implementations were not modified, understanding these behaviors helped clarify the importance of proper system configuration and error handling in UAV software systems.

**UI/UX Enhancement Results:**
Significant improvements were observed in user interface clarity for ground control and dashboard applications. By supporting UI/UX enhancements, it was found that changes in layout, grouping of data fields, and visual prioritization can significantly improve operator understanding. These improvements reduced confusion during monitoring sessions and helped operators respond more effectively during testing. User feedback indicated that the enhanced interfaces made it easier to identify critical information quickly and make informed decisions.

**Automation and Real-Time Data Monitoring:**
Involvement in automation and real-time data monitoring tasks highlighted the importance of accurate data logging and performance tracking. Experiments showed that even small inconsistencies in data handling can have noticeable effects on system evaluation. Automation scripts developed during the internship helped streamline testing procedures and reduce manual effort. Real-time monitoring systems were validated to ensure they could handle data streams without significant delays or data loss.

**System Integration Testing:**
Various integration tests were performed to ensure that different software components worked together correctly. This included testing communication between ground control software and drone systems, verifying data flow through different processing stages, and ensuring that user interface updates reflected actual system status accurately.

**Results Analysis:**
The results demonstrated that reliable drone operation depends heavily on well-maintained software systems, even when working with internal tools rather than production-level applications. Key findings included:

1. **Data Reliability**: Proper implementation of communication protocols and data handling mechanisms is essential for system reliability
2. **User Experience**: UI/UX improvements significantly impact operator effectiveness and reduce errors
3. **Automation Benefits**: Automation scripts and monitoring systems improve efficiency and consistency in testing and data collection
4. **Integration Challenges**: Ensuring proper integration between different software components requires careful attention to interfaces and data formats

**Discussion:**
The internship work revealed several important insights about software engineering in the drone technology industry. The complexity of integrating hardware and software components became apparent through hands-on experience. The importance of user-centered design in ground control software was emphasized through UI/UX improvement work. The value of automation and monitoring systems in maintaining system quality was demonstrated through practical implementation.

Challenges encountered during the work included adapting to complex existing systems, dealing with real-time data variability, and working within the constraints of an industrial environment. These challenges provided valuable learning opportunities and insights into professional software development practices.

The work performed during the internship contributed to improving internal software tools and systems, which in turn supported more efficient drone testing and development processes. While the scope was limited to supporting and assisting tasks, the experience provided comprehensive exposure to real-world software engineering challenges and solutions.

---

# Chapter 5 Conclusions

## 5.1 Summary

The Software Engineering Internship at FlyMek Drone Manufacturing provided valuable practical exposure to real-world software systems used in drone technology. Throughout the internship period from 14 September 2025 to 15 December 2025, work was performed in several key areas including software development and maintenance, communication protocol integration support, UI/UX improvements, and automation and data monitoring activities.

The internship successfully achieved its objectives by providing hands-on experience with internal software systems, MAVLink communication protocols, ground control software like QGroundControl, and real-time data monitoring systems. The work contributed to improving system usability, reliability, and efficiency while providing comprehensive learning opportunities in professional software engineering practices.

Key accomplishments included supporting improvements to user interfaces, assisting in protocol integration, developing automation scripts, and participating in system testing and validation. The internship helped bridge the gap between academic learning and professional practice by allowing application of theoretical knowledge in a real industrial environment.

## 5.2 Limitations

Several limitations were encountered during the internship period:

1. **Access Restrictions**: As an intern, access to certain system components was restricted due to operational and security considerations. The role was limited to assisting and supporting tasks rather than making major architectural changes.

2. **Scope Constraints**: The internship focused on internal tools and support systems rather than flight-critical firmware development, which limited exposure to certain aspects of drone software systems.

3. **Time Constraints**: Adapting to complex existing software systems within a limited time frame was challenging. Understanding system structure and behavior required careful observation and guidance from experienced engineers.

4. **System Variability**: Working with real-time telemetry data presented challenges as system behavior could vary depending on environmental conditions, system load, or hardware configuration, making it difficult to reproduce certain issues consistently.

5. **Limited Documentation**: Some existing systems had limited documentation, requiring reliance on guidance from team members and hands-on exploration to understand functionality.

Despite these limitations, the internship provided meaningful learning opportunities and exposed valuable insights into real-world engineering constraints that are rarely encountered in academic environments.

## 5.3 Future Improvement

Based on the internship experience, several areas for future improvement are suggested:

1. **Enhanced Documentation**: Developing more comprehensive documentation for internal software systems would facilitate faster onboarding and knowledge transfer for new team members and interns.

2. **Structured Onboarding**: Implementing a more formal onboarding process with initial training sessions on software systems and development practices would help interns become productive more quickly.

3. **Expanded Scope**: Providing opportunities for interns to work on more diverse projects, including exposure to flight-critical systems (under appropriate supervision), would enhance learning experiences.

4. **Mentorship Program**: Establishing a formal mentorship program where interns are paired with senior engineers could provide more structured guidance and learning opportunities.

5. **Technology Updates**: Regularly updating development tools and frameworks to stay current with industry standards would improve development efficiency and maintain modern practices.

6. **Knowledge Sharing**: Organizing regular knowledge-sharing sessions where team members present on different topics could help spread expertise and provide learning opportunities.

7. **Testing Infrastructure**: Enhancing automated testing infrastructure would improve system reliability and reduce manual testing effort.

8. **User Feedback Integration**: Establishing more formal processes for collecting and integrating user feedback into UI/UX improvements would enhance user satisfaction and system usability.

These improvements would enhance both the internship experience for future participants and the overall effectiveness of the software development processes at the organization.

---

# References

1. J. M. Anderson, "Unmanned Aerial Vehicles: An Overview," *IEEE Aerospace and Electronic Systems Magazine*, vol. 28, no. 5, pp. 4-11, 2013.

2. L. Mejias, P. Correa, and J. Mondragon, "Collision Avoidance for Unmanned Aerial Vehicles," *IEEE Transactions on Aerospace and Electronic Systems*, vol. 50, no. 3, pp. 1808-1818, 2014.

3. S. H. Kim, H. J. Jeon, and J. H. Kim, "Ground Control Station Software for Unmanned Aerial Vehicles," *International Conference on Control, Automation and Systems*, Seoul, South Korea, pp. 1234-1239, 2011.

4. MAVLink Development Team. "MAVLink Micro Air Vehicle Communication Protocol." Accessed on: Dec. 10, 2025. [Online]. Available: https://mavlink.io/

5. A. P. Schoellig, F. L. Mueller, and R. D'Andrea, "Optimization-based iterative learning for precise quadrocopter trajectory tracking," *Autonomous Robots*, vol. 33, no. 1-2, pp. 103-127, 2012.

6. QGroundControl Development Team. "QGroundControl Ground Control Station." Accessed on: Dec. 10, 2025. [Online]. Available: https://qgroundcontrol.com/

7. M. A. Goodrich, B. S. Morse, D. Gerhardt, J. L. Cooper, M. Quigley, J. A. Adams, and C. Humphrey, "Supporting wilderness search and rescue using a camera-equipped mini UAV," *Journal of Field Robotics*, vol. 25, no. 1-2, pp. 89-110, 2008.

8. R. W. Beard and T. W. McLain, "Small Unmanned Aircraft: Theory and Practice," Princeton University Press, 2012.

9. P. Doherty and P. Rudol, "A UAV search and rescue scenario with human body detection and geolocalization," *Australian Joint Conference on Artificial Intelligence*, Gold Coast, Australia, pp. 1-11, 2007.

10. Y. Gu, M. Kamel, and R. Siegwart, "Unified framework for automated inspection using unmanned aerial vehicles," *IEEE International Conference on Robotics and Automation*, Stockholm, Sweden, pp. 3001-3008, 2016.
