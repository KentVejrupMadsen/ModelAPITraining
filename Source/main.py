from application \
    import ApplicationFramework

def main():
    framework = ApplicationFramework()
    
    framework.initialise()
    framework.execute()
    framework.garbage()

if __name__ == '__main__':
    main()